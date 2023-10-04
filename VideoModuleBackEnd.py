import tensornets as nets
import cv2
import numpy as np
import tensorflow.compat.v1 as tf
from keras.models import load_model
from tensorflow.python.keras.backend import get_session


tf.disable_v2_behavior()

# Image size must be '416x416'
# because Yolo V3 only except network expects that image size
img_size = 416
confidence_level = 0.40
classes = {1: 'bicycle', 2: 'car', 3: 'motorbike', 5: 'bus', 7: 'truck'}

inputs = tf.placeholder(tf.float32, [None, img_size, img_size, 3])
model = nets.YOLOv3COCO(inputs, nets.Darknet19)

sess = tf.Session()
sess.run(model.pretrained())


def Draw_Rectangle(img, pt1, pt2, color, thickness, width_scale=1, height_scale=1):
    point1 = (int(pt1[0] * width_scale), int(pt1[1] * height_scale))
    point2 = (int(pt2[0] * width_scale), int(pt2[1] * height_scale))
    return cv2.rectangle(img, point1, point2, color, thickness)


def Draw_Text(img, text, pt, font, font_scale, color, lineType, width_scale=1,
              height_scale=1):
    pt = (int(pt[0] * width_scale), int(pt[1] * height_scale))
    cv2.putText(img, text, pt, font, font_scale, color, lineType)


def Draw_Circle(img, center, radius, color, thickness, width_scale=1, height_scale=1):
    center = (int(center[0] * width_scale), int(center[1] * height_scale))
    cv2.circle(img, center, radius, color, thickness)


def count_no_of_vehicles_with_yolo(frame):
    total_vehicles = 0

    img = cv2.resize(frame, (img_size, img_size))

    output_img = frame if False else img

    np_img = np.array(img).reshape(-1, img_size, img_size, 3)

    predictions = sess.run(model.preds, {inputs: model.preprocess(np_img)})

    detections = model.get_boxes(predictions, np_img.shape[1:3])
    np_detections = np.array(detections)

    # Loop only through classes we are interested in
    for class_index in classes.keys():
        class_name = classes[class_index]

        # Loop through detected infos of a class we are interested in
        for i in range(len(np_detections[class_index])):
            box = np_detections[class_index][i]

            if np_detections[class_index][i][4] >= confidence_level:
                # print("Detected ", class_name, " with confidence of ", np_detections[class_index][i][4])

                total_vehicles += 1
                startX, startY, endX, endY = box[0], box[1], box[2], box[3]

                Draw_Rectangle(output_img, (startX, startY), (endX, endY), (0, 255, 0), 1)
                Draw_Text(output_img, class_name, (startX, startY), cv2.FONT_HERSHEY_SIMPLEX, .5,
                          (0, 0, 255), 1)

    # Display the total count so far
    Draw_Text(output_img, "Total Vehicle : " + str(total_vehicles), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
              (0, 0, 255), 1)

    return output_img, total_vehicles

    # # Display the current frame (with all annotations drawn up to this point)
    # cv2.imshow("Output", output_img)
    # while True:
    #     key = cv2.waitKey(1) & 0xFF
    #     if key == ord('q'):  # QUIT (exits)
    #         break
    #     elif key == ord('p'):
    #         cv2.waitKey(0)  # PAUSE (Enter any key to continue)


## Code For Ambulance Detection
class Model:
    @staticmethod
    def loadmodel(path):
        return load_model(path)

    def __init__(self, path):
        self.model = self.loadmodel(path)
        self.graph = tf.get_default_graph()

    def predict(self, X):
        with self.graph.as_default():
            return self.model.predict(X)

class AlexNetModel:

    def __init__(self, model_path):

        self.cnn_model = load_model(model_path)
        # self.cnn_model.predict(np.array([[0,0]])) # warmup
        self.session = get_session()
        self.graph = tf.get_default_graph()
        # self.graph.finalize() # finalize


    def query_alexnet(self, data):
        with self.session.as_default():
            with self.graph.as_default():
                prediction = self.cnn_model.predict(data)
        return prediction


li = ['Emergency_Vehicles', 'Non_Emergency_Vehicle']
Ambulance_Detector_Model = AlexNetModel(r'model\AlextNet.hdf5')


def detect_ambulance(frame):
    img1 = cv2.resize(frame, (256, 256))
    img1 = np.expand_dims(img1, axis=0)
    img1 = img1 / 255
    prediction = Ambulance_Detector_Model.query_alexnet(img1)
    d = prediction.flatten()
    j = d.max()
    for index, item in enumerate(d):
        if item == j:
            return li[index]

            # print("\n\nFollowing is our prediction: \n", class_name)
            # print(prediction[0])


def FrameAnalyzer(frame):
    return count_no_of_vehicles_with_yolo(frame), detect_ambulance(frame)

# print(Analyzer('test1.jpg'))
