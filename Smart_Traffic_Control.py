import sys
import tkinter as tk
import os.path
import cv2
import TIMER_Algorithm
from PIL import ImageTk, Image
from VideoModuleBackEnd import FrameAnalyzer
from tkinter import filedialog, messagebox

# from multiprocessing.pool import ThreadPool
# pool = ThreadPool(processes=4)

import threading
import cv2
import time
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1(root)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):

        self.LaneOneVideoPath = None
        self.LaneTwoVideoPath = None
        self.LaneThreeVideoPath = None
        self.LaneFourVideoPath = None
        self.SkipFrameRate = 8
        self.Lane_One_Result = None
        self.Lane_Two_Result = None
        self.Lane_Three_Result = None
        self.Lane_Four_Result = None
        self.Lan_One_AM = False
        self.Lan_Two_AM = False
        self.Lan_Three_AM = False
        self.Lan_Four_AM = False

        def ProcessLanOneVideo():
            frame_count = 0
            VideoSourceLanOne = cv2.VideoCapture(self.LaneOneVideoPath)
            print('Processing Thread One ',self.LaneOneVideoPath)
 
            Amb_counter = 0

            while True:
                _, frame = VideoSourceLanOne.read()
                if _:
                    if frame_count != self.SkipFrameRate:
                        frame_count = frame_count + 1
                        pass
                    else:
                        self.Lane_One_Result = FrameAnalyzer(frame)
                        cv2image = cv2.cvtColor(self.Lane_One_Result[0][0], cv2.COLOR_BGR2RGBA)

                        # if self.Lane_One_Result==None:
                        #     self.Lane_One_Result = FrameAnalyzer(frame)
                        #     cv2image = cv2.cvtColor(self.Lane_One_Result[0][0], cv2.COLOR_BGR2RGBA)
                        # else:
                        #     Lane_One_Result = FrameAnalyzer(frame)
                        #     cv2image = cv2.cvtColor(Lane_One_Result[0][0], cv2.COLOR_BGR2RGBA)

                        imgtk = ImageTk.PhotoImage(image=Image.fromarray(cv2image).resize((550, 300)))
                        self.lblLaneOneMedia.imgtk = imgtk
                        self.lblLaneOneMedia.configure(image=imgtk)

                        time.sleep(0.005)
                        frame_count = 0



        def ProcessLanTwoVideo():
            frame_count = 0
            VideoSourceLanTwo = cv2.VideoCapture(self.LaneTwoVideoPath)
            print('Processing Thread Two ',self.LaneTwoVideoPath)
 
            while True:
                _, frame = VideoSourceLanTwo.read()
                if _:
                    if frame_count != self.SkipFrameRate:
                        frame_count = frame_count + 1
                        pass
                    else:
                        self.Lane_Two_Result = FrameAnalyzer(frame)
                        cv2image = cv2.cvtColor(self.Lane_Two_Result[0][0], cv2.COLOR_BGR2RGBA)

                        # if self.Lane_Two_Result==None:
                        #     self.Lane_Two_Result = FrameAnalyzer(frame)
                        #     cv2image = cv2.cvtColor(self.Lane_Two_Result[0][0], cv2.COLOR_BGR2RGBA)
                        # else:
                        #     Lane_Two_Result = FrameAnalyzer(frame)
                        #     cv2image = cv2.cvtColor(Lane_Two_Result[0][0], cv2.COLOR_BGR2RGBA)

                        imgtk = ImageTk.PhotoImage(image=Image.fromarray(cv2image).resize((550, 300)))
                        self.lblLaneTwoMedia.imgtk = imgtk
                        self.lblLaneTwoMedia.configure(image=imgtk)

                        time.sleep(0.005)
                        frame_count = 0



        def ProcessLanThreeVideo():
            frame_count = 0
            VideoSourceLanThree = cv2.VideoCapture(self.LaneThreeVideoPath)
            print('Processing Thread Three ',self.LaneThreeVideoPath)
 
            while True:
                _, frame = VideoSourceLanThree.read()
                if _:
                    if frame_count != self.SkipFrameRate:
                        frame_count = frame_count + 1
                        pass
                    else:
                        self.Lane_Three_Result = FrameAnalyzer(frame)
                        cv2image = cv2.cvtColor(self.Lane_Three_Result[0][0], cv2.COLOR_BGR2RGBA)

                        # if self.Lane_Three_Result==None:
                        #     self.Lane_Three_Result = FrameAnalyzer(frame)
                        #     cv2image = cv2.cvtColor(self.Lane_Three_Result[0][0], cv2.COLOR_BGR2RGBA)
                        # else:
                        #     Lane_Three_Result = FrameAnalyzer(frame)
                        #     cv2image = cv2.cvtColor(Lane_Three_Result[0][0], cv2.COLOR_BGR2RGBA)

                        imgtk = ImageTk.PhotoImage(image=Image.fromarray(cv2image).resize((550, 300)))
                        self.lblLaneThreeMedia.imgtk = imgtk
                        self.lblLaneThreeMedia.configure(image=imgtk)

                        time.sleep(0.005)
                        frame_count = 0



        def ProcessLanFourVideo():
            frame_count = 0
            VideoSourceLanFour = cv2.VideoCapture(self.LaneFourVideoPath)
            print('Processing Thread Four ',self.LaneFourVideoPath)
            while True:
                _, frame = VideoSourceLanFour.read()
                if _:
                    if frame_count != self.SkipFrameRate:
                        frame_count = frame_count + 1
                        pass
                    else:
                        self.Lane_Four_Result = FrameAnalyzer(frame)
                        cv2image = cv2.cvtColor(self.Lane_Four_Result[0][0], cv2.COLOR_BGR2RGBA)

                        # if self.Lane_Four_Result==None:
                        #     self.Lane_Four_Result = FrameAnalyzer(frame)
                        #     cv2image = cv2.cvtColor(self.Lane_Four_Result[0][0], cv2.COLOR_BGR2RGBA)
                        # else:
                        #     Lane_Four_Result = FrameAnalyzer(frame)
                        #     cv2image = cv2.cvtColor(Lane_Four_Result[0][0], cv2.COLOR_BGR2RGBA)

                        imgtk = ImageTk.PhotoImage(image=Image.fromarray(cv2image).resize((550, 300)))
                        self.lblLaneFourMedia.imgtk = imgtk
                        self.lblLaneFourMedia.configure(image=imgtk)

                        time.sleep(0.005)
                        frame_count = 0



        def SetPrority():
            while True:
                if self.Lane_One_Result==None or self.Lane_Two_Result==None or self.Lane_Three_Result==None or self.Lane_Four_Result==None:
                    pass
                else:
                    print('\n\nProcessing for timing')

                    time_req = TIMER_Algorithm.Calculate_Time_Required(
                        self.Lane_One_Result[0][1],
                        self.Lane_Two_Result[0][1],
                        self.Lane_Three_Result[0][1],
                        self.Lane_Four_Result[0][1],
                    )

                    temp_time_req = TIMER_Algorithm.Calculate_Time_Required(
                        self.Lane_One_Result[0][1],
                        self.Lane_Two_Result[0][1],
                        self.Lane_Three_Result[0][1],
                        self.Lane_Four_Result[0][1],
                    )

                    Lan_One_AM = False
                    Lan_Two_AM = False
                    Lan_Three_AM = False
                    Lan_Four_AM = False

                    if self.Lane_One_Result[1] == 'Emergency_Vehicles':
                        Lan_One_AM = True
                    if self.Lane_Two_Result[1] == 'Emergency_Vehicles':
                        Lan_Two_AM = True
                    if self.Lane_Three_Result[1] == 'Emergency_Vehicles':
                        Lan_Three_AM = True
                    if self.Lane_Four_Result[1] == 'Emergency_Vehicles':
                        Lan_Four_AM = True

                    priority = {}
                    priority_set_for = []
                    priority_do_not_set_for = [1,2,3,4]

                    Ambulance_count = 0
                    if Lan_One_AM:
                        priority_set_for.append(1)
                        priority_do_not_set_for.remove(1)
                        time_req.pop(0)
                        Ambulance_count = Ambulance_count + 1
                        priority['Lane 1'] = len(priority) + 1

                    if Lan_Two_AM:
                        priority_set_for.append(2)
                        priority_do_not_set_for.remove(2)
                        time_req.pop(Ambulance_count - 1)
                        Ambulance_count = Ambulance_count + 1
                        priority['Lane 2'] = len(priority) + 1

                    if Lan_Three_AM:
                        priority_set_for.append(3)
                        priority_do_not_set_for.remove(3)
                        time_req.pop(Ambulance_count - 2)
                        Ambulance_count = Ambulance_count + 1
                        priority['Lane 3'] = len(priority) + 1

                    if Lan_Four_AM:
                        priority_set_for.append(4)
                        priority_do_not_set_for.remove(4)
                        time_req.pop(Ambulance_count - 3)
                        Ambulance_count = Ambulance_count + 1
                        priority['Lane 4'] = len(priority) + 1


                    for i in range(len(priority_do_not_set_for)):
                        max_value = max(time_req)
                        index = time_req.index(max_value)
                        lane_no = priority_do_not_set_for[index]
                        time_req.remove(max_value)
                        priority_do_not_set_for.pop(index)
                        priority['Lane '+str(lane_no)] = len(priority) + 1


                    # print(str(priority.get('Lane 1')))
                    # print(str(Lane_One_Result[0][1]))
                    # print(temp_time_req)
                    # print(str(temp_time_req[0]))

                    if Lan_One_AM:
                        lane__one_text = 'Lane 1,  P: '+str(priority.get('Lane 1'))+ ',   TV : '+ str(self.Lane_One_Result[0][1]) +' ,   EV : 1,    ETR : '+str(int(temp_time_req[0]))+' Sec'
                    else:
                        lane__one_text = 'Lane 1,  P: '+str(priority.get('Lane 1'))+ ',   TV : '+ str(self.Lane_One_Result[0][1]) +' ,   EV : 0,    ETR : '+str(int(temp_time_req[0]))+' Sec'

                    if Lan_Two_AM:
                        lane__two_text = 'Lane 2,  P: '+str(priority.get('Lane 2'))+ ',   TV : '+ str(self.Lane_Two_Result[0][1]) +' ,   EV : 1,    ETR : '+str(int(temp_time_req[1]))+' Sec'
                    else:
                        lane__two_text = 'Lane 2,  P: '+str(priority.get('Lane 2'))+ ',   TV : '+ str(self.Lane_Two_Result[0][1]) +' ,   EV : 0,    ETR : '+str(int(temp_time_req[1]))+' Sec'


                    if Lan_Three_AM:
                        lane__Three_text = 'Lane 3,  P: '+str(priority.get('Lane 3'))+ ',   TV : '+ str(self.Lane_Three_Result[0][1]) +' ,   EV : 1,    ETR : '+str(int(temp_time_req[2]))+' Sec'
                    else:
                        lane__Three_text = 'Lane 3,  P: '+str(priority.get('Lane 3'))+ ',   TV : '+ str(self.Lane_Three_Result[0][1]) +' ,   EV : 0,    ETR : '+str(int(temp_time_req[2]))+' Sec'


                    if Lan_Four_AM:
                        lane__Four_text = 'Lane 4,  P: '+str(priority.get('Lane 4'))+ ',   TV : '+ str(self.Lane_Four_Result[0][1]) +' ,   EV : 1,    ETR : '+str(int(temp_time_req[3])) +' Sec'
                    else:
                        lane__Four_text = 'Lane 4,  P: '+str(priority.get('Lane 4'))+ ',   TV : '+ str(self.Lane_Four_Result[0][1]) +' ,   EV : 0,    ETR : '+str(int(temp_time_req[3]))+' Sec'


                    self.lblLaneOneResult.configure(text=lane__one_text)
                    self.lblLaneTwoResult.configure(text=lane__two_text)
                    self.lblLaneThreeResult.configure(text=lane__Three_text)
                    self.lblLaneFourResult.configure(text=lane__Four_text)

                    time.sleep(20)





        def selectLaneOneMedia(event):
            ##Get File directory from user
            VideoFileName = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(
                ("mp4 files", "*.mp4"), ("png files", "*.png"), ("all files", "*.*")))
            self.LaneOneVideoPath = VideoFileName
            self.lblLaneOneMedia.configure(text=VideoFileName)

        def selectLaneTwoMedia(event):
            ##Get File directory from user
            VideoFileName = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(
                ("mp4 files", "*.mp4"), ("png files", "*.png"), ("all files", "*.*")))
            self.LaneTwoVideoPath = VideoFileName
            self.lblLaneTwoMedia.configure(text=VideoFileName)


        def selectLaneThreeMedia(event):
            ##Get File directory from user
            VideoFileName = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(
                ("mp4 files", "*.mp4"), ("png files", "*.png"), ("all files", "*.*")))
            self.LaneThreeVideoPath = VideoFileName
            self.lblLaneThreeMedia.configure(text=VideoFileName)

        def selectLaneFourMedia(event):
            ##Get File directory from user
            VideoFileName = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(
                ("mp4 files", "*.mp4"), ("png files", "*.png"), ("all files", "*.*")))
            self.LaneFourVideoPath = VideoFileName
            self.lblLaneFourMedia.configure(text=VideoFileName)


        def Get_Color_And_Resize_Image(DetetectObjectImage):
            b, g, r = cv2.split(DetetectObjectImage)
            rbgImg = cv2.merge((r, g, b))
            image = Image.fromarray(rbgImg)
            image = image.resize((550, 300), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            return photo

        def btnCalculateResult(event):
            if (self.LaneOneVideoPath == None):
                messagebox.showerror('Lan 1 Missing', 'No Media Found at Lan 1')
                return
            if (self.LaneTwoVideoPath == None):
                messagebox.showerror('Lan 2 Missing', 'No Media Found at Lan 2')
                return

            if (self.LaneThreeVideoPath == None):
                messagebox.showerror('Lan 3 Missing', 'No Media Found at Lan 3')
                return

            if (self.LaneFourVideoPath == None):
                messagebox.showerror('Lan 4 Missing', 'No Media Found at Lan 4')
                return

            threading.Thread(target=ProcessLanOneVideo).start()
            threading.Thread(target=ProcessLanTwoVideo).start()
            threading.Thread(target=ProcessLanThreeVideo).start()
            threading.Thread(target=ProcessLanFourVideo).start()
            threading.Thread(target=SetPrority).start()


        def exit_top(event):
            top.destroy()
            import Smart_Traffic_Control
            Smart_Traffic_Control.vp_start_gui()



            # Time_Required = TIMER_Algorithm.Calculate_Time_Required(
            #     Lane_One_Result[0][1],
            #     Lane_Two_Result[0][1],
            #     Lane_Three_Result[0][1],
            #     Lane_Four_Result[0][1],
            # )
            #
            # self.lblLaneOneResult.configure(text="Time Required : "+str(Time_Required[0])[:4])
            # self.lblLaneTwoResult.configure(text="Time Required : "+str(Time_Required[1])[:4])
            # self.lblLaneThreeResult.configure(text="Time Required : "+str(Time_Required[2])[:4])
            # self.lblLaneFourResult.configure(text="Time Required : "+str(Time_Required[3])[:4])


        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 14 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font11 = "-family {Sitka Small} -size 19 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font12 = "-family {Times New Roman} -size 36 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font14 = "-family {Sitka Small} -size 13 -weight normal -slant" \
                 " roman -underline 0 -overstrike 0"

        top.geometry("1571x1010+26+5")
        top.title("New Toplevel")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.state("zoomed")
        top.bind("<Escape>", exit_top)


        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.003, rely=0.089, height=774, width=1564)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location, "gui_images\\lane_back_2.png")
        self._img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=self._img0)
        self.Label1.configure(text='''Label''')
        self.Label1.configure(width=1564)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.21, rely=0.01, height=73, width=907)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Congestion Control System''')
        self.Label2.configure(width=907)

        self.lblLaneOneMedia = tk.Label(top)
        self.lblLaneOneMedia.place(relx=0.022, rely=0.114, height=296, width=552)

        self.lblLaneOneMedia.configure(activebackground="#f9f9f9")
        self.lblLaneOneMedia.configure(activeforeground="black")
        self.lblLaneOneMedia.configure(background="#ffffff")
        self.lblLaneOneMedia.configure(disabledforeground="#a3a3a3")
        self.lblLaneOneMedia.configure(font=font14)
        self.lblLaneOneMedia.configure(foreground="#000000")
        self.lblLaneOneMedia.configure(highlightbackground="#d9d9d9")
        self.lblLaneOneMedia.configure(highlightcolor="black")
        self.lblLaneOneMedia.configure(relief="groove")
        self.lblLaneOneMedia.configure(text='''Select Lane 1 Media''')
        self.lblLaneOneMedia.configure(width=552)
        self.lblLaneOneMedia.bind('<Button-1>', selectLaneOneMedia)

        self.lblLaneTwoMedia = tk.Label(top)
        self.lblLaneTwoMedia.place(relx=0.595, rely=0.114, height=296, width=552)
        self.lblLaneTwoMedia.configure(activebackground="#f9f9f9")
        self.lblLaneTwoMedia.configure(activeforeground="black")
        self.lblLaneTwoMedia.configure(background="#ffffff")
        self.lblLaneTwoMedia.configure(disabledforeground="#a3a3a3")
        self.lblLaneTwoMedia.configure(font=font14)
        self.lblLaneTwoMedia.configure(foreground="#000000")
        self.lblLaneTwoMedia.configure(highlightbackground="#d9d9d9")
        self.lblLaneTwoMedia.configure(highlightcolor="black")
        self.lblLaneTwoMedia.configure(relief="groove")
        self.lblLaneTwoMedia.configure(text='''Select Lan 2 Media''')
        self.lblLaneTwoMedia.bind('<Button-1>', selectLaneTwoMedia)

        self.lblLaneThreeMedia = tk.Label(top)
        self.lblLaneThreeMedia.place(relx=0.019, rely=0.635, height=296
                                     , width=552)
        self.lblLaneThreeMedia.configure(activebackground="#f9f9f9")
        self.lblLaneThreeMedia.configure(activeforeground="black")
        self.lblLaneThreeMedia.configure(background="#ffffff")
        self.lblLaneThreeMedia.configure(disabledforeground="#a3a3a3")
        self.lblLaneThreeMedia.configure(font=font14)
        self.lblLaneThreeMedia.configure(foreground="#000000")
        self.lblLaneThreeMedia.configure(highlightbackground="#d9d9d9")
        self.lblLaneThreeMedia.configure(highlightcolor="black")
        self.lblLaneThreeMedia.configure(relief="groove")
        self.lblLaneThreeMedia.configure(text='''Select Lane 3 Media''')
        self.lblLaneThreeMedia.bind('<Button-1>', selectLaneThreeMedia)

        self.lblLaneFourMedia = tk.Label(top)
        self.lblLaneFourMedia.place(relx=0.602, rely=0.635, height=296
                                    , width=552)
        self.lblLaneFourMedia.configure(activebackground="#f9f9f9")
        self.lblLaneFourMedia.configure(activeforeground="black")
        self.lblLaneFourMedia.configure(background="#ffffff")
        self.lblLaneFourMedia.configure(disabledforeground="#a3a3a3")
        self.lblLaneFourMedia.configure(font=font14)
        self.lblLaneFourMedia.configure(foreground="#000000")
        self.lblLaneFourMedia.configure(highlightbackground="#d9d9d9")
        self.lblLaneFourMedia.configure(highlightcolor="black")
        self.lblLaneFourMedia.configure(relief="groove")
        self.lblLaneFourMedia.configure(text='''Select Lan 4 Media''')
        self.lblLaneFourMedia.bind('<Button-1>', selectLaneFourMedia)

        self.lblLaneOneResult = tk.Label(top)
        self.lblLaneOneResult.place(relx=0.025, rely=0.516, height=26, width=542)
        self.lblLaneOneResult.configure(activebackground="#f9f9f9")
        self.lblLaneOneResult.configure(activeforeground="black")
        self.lblLaneOneResult.configure(background="#000000")
        self.lblLaneOneResult.configure(disabledforeground="#a3a3a3")
        self.lblLaneOneResult.configure(font=font10)
        self.lblLaneOneResult.configure(foreground="#ffffff")
        self.lblLaneOneResult.configure(highlightbackground="#d9d9d9")
        self.lblLaneOneResult.configure(highlightcolor="black")
        self.lblLaneOneResult.configure(text='''Lane 1,  P: ,   TV :  ,   EV : ,    ETR : Sec''')
        self.lblLaneOneResult.configure(width=542)

        self.lblLaneTwoResult = tk.Label(top)
        self.lblLaneTwoResult.place(relx=0.598, rely=0.516, height=26, width=552)

        self.lblLaneTwoResult.configure(activebackground="#f9f9f9")
        self.lblLaneTwoResult.configure(activeforeground="black")
        self.lblLaneTwoResult.configure(background="#000000")
        self.lblLaneTwoResult.configure(disabledforeground="#a3a3a3")
        self.lblLaneTwoResult.configure(font=font10)
        self.lblLaneTwoResult.configure(foreground="#ffffff")
        self.lblLaneTwoResult.configure(highlightbackground="#d9d9d9")
        self.lblLaneTwoResult.configure(highlightcolor="black")
        self.lblLaneTwoResult.configure(text='''Lane 2,  P:,   TV :  ,   EV : ,    ETR :  Sec''')
        self.lblLaneTwoResult.configure(width=552)

        self.lblLaneThreeResult = tk.Label(top)
        self.lblLaneThreeResult.place(relx=0.025, rely=0.57, height=26, width=542)
        self.lblLaneThreeResult.configure(activebackground="#f9f9f9")
        self.lblLaneThreeResult.configure(activeforeground="black")
        self.lblLaneThreeResult.configure(background="#000000")
        self.lblLaneThreeResult.configure(disabledforeground="#a3a3a3")
        self.lblLaneThreeResult.configure(font=font10)
        self.lblLaneThreeResult.configure(foreground="#ffffff")
        self.lblLaneThreeResult.configure(highlightbackground="#d9d9d9")
        self.lblLaneThreeResult.configure(highlightcolor="black")
        self.lblLaneThreeResult.configure(text='''Lane 3,  P:,   TV :  ,   EV : ,    ETR :  Sec''')
        self.lblLaneThreeResult.configure(width=542)

        self.lblLaneFourResult = tk.Label(top)
        self.lblLaneFourResult.place(relx=0.598, rely=0.57, height=26, width=552)
        self.lblLaneFourResult.configure(activebackground="#f9f9f9")
        self.lblLaneFourResult.configure(activeforeground="black")
        self.lblLaneFourResult.configure(background="#000000")
        self.lblLaneFourResult.configure(disabledforeground="#a3a3a3")
        self.lblLaneFourResult.configure(font=font10)
        self.lblLaneFourResult.configure(foreground="#ffffff")
        self.lblLaneFourResult.configure(highlightbackground="#d9d9d9")
        self.lblLaneFourResult.configure(highlightcolor="black")
        self.lblLaneFourResult.configure(text='''Lane 4,  P:,  TV :  ,   EV : ,    ETR :  Sec''')
        self.lblLaneFourResult.configure(width=552)

        self.btnCalculateTiming = tk.Button(top)
        self.btnCalculateTiming.place(relx=0.423, rely=0.52, height=63
                                      , width=206)
        self.btnCalculateTiming.configure(activebackground="#ececec")
        self.btnCalculateTiming.configure(activeforeground="#d7def7")
        self.btnCalculateTiming.configure(background="#a1e9ff")
        self.btnCalculateTiming.configure(disabledforeground="#a3a3a3")
        self.btnCalculateTiming.configure(font=font11)
        self.btnCalculateTiming.configure(foreground="#ffffff")
        self.btnCalculateTiming.configure(highlightbackground="#d9d9d9")
        self.btnCalculateTiming.configure(highlightcolor="black")
        self.btnCalculateTiming.configure(pady="0")
        self.btnCalculateTiming.configure(text='''Calculate''')
        self.btnCalculateTiming.configure(width=206)
        self.btnCalculateTiming.bind('<Button-1>', btnCalculateResult)


if __name__ == '__main__':
    vp_start_gui()



# https://stackoverflow.com/questions/46725323/keras-tensorflow-exception-while-predicting-from-multiple-threads#:~:text=_make_predict_function()%20on%20a%20keras,slower%20than%20every%20other%20time.
# https://stackoverflow.com/questions/65876044/how-display-multi-videos-with-threading-using-tkinter-in-python
# https://www.geeksforgeeks.org/extract-images-from-video-in-python/

