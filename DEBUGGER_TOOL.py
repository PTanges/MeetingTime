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

