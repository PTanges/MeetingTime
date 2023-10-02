def flagUnavailableTimes(availableTimes, workerMeetingTimes, workerScheduledHours):
    _flagScheduledHours(availableTimes, workerScheduledHours)
    _flagScheduledMeetings(availableTimes, workerMeetingTimes)

def _flagScheduledHours(availableTimes, workerScheduledHours):
    # Note: Parser below accounts for both 09:00 and 9:00 format
    _analogTime = []
    _hoursMinutesStrings = []

    for block in workerScheduledHours:
        _splitBlock = block.split(",") # 9:00 | 19:00 | 9:00 | 17:00
        _analogTime.append(_splitBlock[0])
        _analogTime.append(_splitBlock[1])

    for time in _analogTime:
        _splitTime = time.split(":") # 9 | 00 | 19 | 00 | 9 | 00 | 17 | 00
        _hoursMinutesStrings.append(_splitTime[0])
        _hoursMinutesStrings.append(_splitTime[1])

    # 00:00 to Clock In
    _worker1StartTime = _analogToMinutesHM(_hoursMinutesStrings[0], _hoursMinutesStrings[1])
    _worker2StartTime = _analogToMinutesHM(_hoursMinutesStrings[4], _hoursMinutesStrings[5])
    if (_worker1StartTime >= _worker2StartTime):
        _flagUnavailableTimes(availableTimes, 0, _worker1StartTime)
    else:
        _flagUnavailableTimes(availableTimes, 0, _worker2StartTime)

    # Clock Out to 00:00
    _worker1StartTime = _analogToMinutesHM(_hoursMinutesStrings[2], _hoursMinutesStrings[3])
    _worker2StartTime = _analogToMinutesHM(_hoursMinutesStrings[6], _hoursMinutesStrings[7])
    if (_worker1StartTime >= _worker2StartTime):
        _flagUnavailableTimes(availableTimes, _worker2StartTime, len(availableTimes))
    else:
        _flagUnavailableTimes(availableTimes, _worker1StartTime, len(availableTimes))

def _flagScheduledMeetings(availableTimes, workerMeetingTimes):
    _analogTime = []
    for block in workerMeetingTimes:
        # [9:00 | 10:30] | [12:20 | 14:30] | [14:30 | 15:00] | [16:00 | 17:00]
        _analogTime = block.split(",")

        _meetingStartHours = _analogTime[0]
        _meetingStartMinutes = _analogTime[1]

        _startMinuteIndex = 0
        if len(_meetingStartHours) == 4: # Must be 9:59 or sooner
            _startMinuteIndex = _analogToMinutesHMM(_meetingStartHours[0], _meetingStartHours[2], _meetingStartHours[3])
        else: # Assumes 5 characters
            _startMinuteIndex = _analogToMinutesHHMM(_meetingStartHours[0], _meetingStartHours[1], _meetingStartHours[3], _meetingStartHours[4])

        _endMinuteIndex = 0
        if len(_meetingStartMinutes) == 4: # Must be 9:59 or sooner
            _endMinuteIndex = _analogToMinutesHMM(_meetingStartMinutes[0], _meetingStartMinutes[2], _meetingStartMinutes[3])
        else: # Assumes 5
            _endMinuteIndex = _analogToMinutesHHMM(_meetingStartMinutes[0], _meetingStartMinutes[1], _meetingStartMinutes[3], _meetingStartMinutes[4])

        _flagUnavailableTimes(availableTimes, _startMinuteIndex, _endMinuteIndex)

def _flagUnavailableTimes(availableTimes, startIndex, endIndex):
    _iterations = int(endIndex) - int(startIndex)
    for i in range(_iterations):
        availableTimes[i + startIndex] = False

def scanValidMeetingTimes(availableTimes, minimumMeetingTime, outputTimes):
    # Iterate through the array looking for times of length MMT and store + print
    _validMeetingTimes = "["

    _incrementer = 0
    _startMinute = 0
    _endMinute = 0
    _hasTimeFormat = False
    for i in range (len(availableTimes)):
        if availableTimes[i] is True:
            if _incrementer == 0:
                _startMinute = i # First Continuous True Index
            _incrementer += 1
        else:
            if _incrementer >= minimumMeetingTime:
                _endMinute = i # Last Continuous TRUE Index
                if _hasTimeFormat == True:
                    _validMeetingTimes += ", "
                _validMeetingTimes += _minutesToAnalog(_startMinute, _endMinute)
                _hasTimeFormat = True
            # Reset Continuous Counter
            _incrementer = 0

    if _incrementer >= minimumMeetingTime:
        # Edge case: append occurs only when swap from T -> F & count >= MMT
        # Thus if the end of day is still True, no append occurs
        # Output should read as "[XX:XX, 24:00]
        _endMinute = len(availableTimes)
        if _hasTimeFormat == True:
            _validMeetingTimes += ", "
        _validMeetingTimes += _minutesToAnalog(_startMinute, _endMinute)

    _validMeetingTimes += "]"

    # Print / Write
    outputTimes.append(_validMeetingTimes)

# Time Conversion Helper Functions
# TO DO: Overload functions, remove HM HMM HHMM
def _analogToMinutesHM(hour, minutes):
    time = (int(hour) * 60) + int(minutes)
    return time

def _analogToMinutesHMM(hour, minuteTens, minuteSingle):
    # Single and Tens refer to digit places
    time = (int(hour) * 60) + (int(minuteTens)*10) + (int(minuteSingle))
    return time

def _analogToMinutesHHMM(hourTens, hourSingle, minuteTens, minuteSingle):
    # Single and Tens refer to digit places
    time = (int(hourTens) * 10 * 60) + (int(hourSingle) * 60) + (int(minuteTens)*10) + (int(minuteSingle))
    return time

def _minutesToAnalog(startMinute, endMinute):
    # Returns a String
    _analogTime = ""

    _hourCount = 0
    while startMinute >= 60:
        _hourCount += 1
        startMinute -= 60
    _analogTime += '['
    if _hourCount < 10:
        _analogTime += "0"
        _analogTime += str(_hourCount)
    else:
        _analogTime += str(_hourCount)
    _analogTime += ":"
    if startMinute <= 10:
        _analogTime += "0"
        _analogTime += str(startMinute)
    else:
        _analogTime += str(startMinute)
    # Output: "[09:00"

    _hourCount = 0
    while endMinute >= 60:
        _hourCount += 1
        endMinute -= 60
    _analogTime += ", "
    if _hourCount < 10:
        _analogTime += "0"
        _analogTime += str(_hourCount)
    else:
        _analogTime += str(_hourCount)
    _analogTime += ":"
    if endMinute <= 10:
        _analogTime += "0"
        _analogTime += str(endMinute)
    else:
        _analogTime += str(endMinute)
    _analogTime += "]"
    # Output: "[09:00, 09:30]"
    return _analogTime