def createSampleSchedule():
    ''' Sample Schedule
    [[12:00,13:00],[16:00,18:00]]
    [9:00,19:00]
    [[9:00,10:30],[12:20,14:30],[14:30,15:00],[16:00,17:00]]
    [9:00,18:30]
    30
    '''

    _minimumMeetingTime = 30

    # User may assume that MEETING TIMES are NOT scheduled outside of Working Hours
    file = open("schedule.txt", "w")
    file.write("[[12:00, 13:00], [16:00, 18:00]]\n")
    file.write("[9:00, 19:00]\n")
    file.write("[[9:00, 10:30], [12:20, 14:30], [14:30,15:00], [16:00, 17:00 ]]\n")
    file.write("[9:00, 18:30]\n")
    file.write(str(_minimumMeetingTime))
    file.close()

def createSampleSchedule10():
    # User may assume that MEETING TIMES are NOT scheduled outside of Working Hours
    file = open("schedule.txt", "w")

    file.write("[[12:00, 13:00], [16:00, 18:00]]\n")
    file.write("[9:00, 19:00]\n")
    file.write("[[9:00, 10:30], [12:20, 14:30], [14:30,15:00], [16:00, 17:00 ]]\n")
    file.write("[9:00, 18:30]\n")
    file.write("30\n")

    file.write("[[9:00, 9:30], [16:00, 17:00]]\n")
    file.write("[9:00, 17:00]\n")
    file.write("[[11:45, 13:30], [13:40, 14:21], [14:30, 14:31], [15:00, 17:00]]\n")
    file.write("[11:00, 19:30]\n")
    file.write("45\n")

    file.write("[[12:00, 12:30], [16:00, 17:00]]\n")
    file.write("[12:00, 23:00]\n")
    file.write("[[1:45, 3:30], [3:59, 4:01], [4:30, 4:31], [5:00, 5:01]]\n")
    file.write("[1:00, 5:30]\n")
    file.write("90\n")

    file.write("[[2:00, 3:30], [14:00, 18:00], [18:18, 19:00]]\n")
    file.write("[00:00, 19:00]\n")
    file.write("[[11:05, 11:30], [13:00, 13:21], [13:23, 13:24], [13:27, 13:29]]\n")
    file.write("[11:00, 13:30]\n")
    file.write("21\n")

    file.write("[[5:00, 7:30], [7:31, 7:45]]\n")
    file.write("[2:00, 9:00]\n")
    file.write("[[11:45, 13:30], [13:40, 14:21], [14:30, 14:31], [15:00, 17:00]]\n")
    file.write("[1:11, 21:59]\n")
    file.write("55\n")

    file.write("[[8:11, 8:49], [14:14, 17:17]]\n")
    file.write("[8:00, 20:21]\n")
    file.write("[[1:45, 3:40], [3:59, 14:21]]\n")
    file.write("[1:12, 14:22]\n")
    file.write("10\n")

    file.write("[[9:00, 9:30], [16:00, 17:00]]\n")
    file.write("[9:00, 17:00]\n")
    file.write("[[11:45, 13:30], [15:00, 17:00]]\n")
    file.write("[11:00, 19:30]\n")
    file.write("39\n")

    file.write("[[0:00, 14:30], [14:41, 14:59], [15:01, 15:30], [15:31, 15:45], [16:00, 17:00], [23:00, 23:30]]\n")
    file.write("[0:00, 24:00]\n")
    file.write("[[11:45, 14:40], [15:30, 17:31], [18:01, 19:19]]\n")
    file.write("[0:00, 24:00]\n")
    file.write("72\n")

    file.write("[[0:00, 0:03], [00:05, 0:18]]\n")
    file.write("[0:00, 0:40]\n")
    file.write("[[0:15, 0:16], [0:17, 0:21]]\n")
    file.write("[0:15, 0:52]\n")
    file.write("11\n")

    file.write("[[3:10, 5:50], [12:30, 15:56]]\n")
    file.write("[2:07, 23:12]\n")
    file.write("[[1:16, 1:21], [4:03, 4:41], [5:00, 7:00]]\n")
    file.write("[1:08, 10:33]\n")
    file.write("99\n")

    file.close()