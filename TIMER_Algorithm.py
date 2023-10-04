def Calculate_Time_Required(Lane_One, Lane_Two, Lane_Three, Lane_Four):
    ALL_VEHICLES_COUNT = []
    ALL_VEHICLES_COUNT.append(int(Lane_One))
    ALL_VEHICLES_COUNT.append(int(Lane_Two))
    ALL_VEHICLES_COUNT.append(int(Lane_Three))
    ALL_VEHICLES_COUNT.append(int(Lane_Four))

    TOTAL_TIME_LIMIT = 120
    MIN_MAX_TIME_LIMIT = [5, 30]

    # TOTAL_TIME_LIMIT = int(input("Enter the base timer value"))
    # MIN_MAX_TIME_LIMIT = list(map(int,input("Enter the time limits ").split()))

    print("Input no of vehicles : ", *ALL_VEHICLES_COUNT)
    t = [
        (i / sum(ALL_VEHICLES_COUNT)) * TOTAL_TIME_LIMIT if MIN_MAX_TIME_LIMIT[0] < (
                i / sum(ALL_VEHICLES_COUNT)) * TOTAL_TIME_LIMIT < MIN_MAX_TIME_LIMIT[
                                                                1]
        else min(MIN_MAX_TIME_LIMIT, key=lambda x: abs(x - (i / sum(ALL_VEHICLES_COUNT)) * TOTAL_TIME_LIMIT)) for i in
        ALL_VEHICLES_COUNT]

    return t
    # print(t, sum(t))


# print(Calculate_Time_Required(10,50,2,3))


# ALL_VEHICLES_COUNT = []
# ALL_VEHICLES_COUNT.append(int(input('Enter LANE 1 vehicle count : ')))
# ALL_VEHICLES_COUNT.append(int(input('Enter LANE 2 vehicle count : ')))
# ALL_VEHICLES_COUNT.append(int(input('Enter LANE 3 vehicle count : ')))
# ALL_VEHICLES_COUNT.append(int(input('Enter LANE 4 vehicle count : ')))
