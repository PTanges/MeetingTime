import os
import MT_COMPUTATION

def parseFile(inputFileName, outputTimes):
    # File Deliminator between Samples is finding the minimumMeetingTime

    # Local Variables
    _timeSpanString = ""
    _workerMeetingTimes = []
    _workerScheduledHours = [] # Example: 9AM-5PM, written as [09:00,17:00]

    # Loop 1440 times with bool True
    _availableTimes = []
    _fillBoolAvailableTime(_availableTimes)

    # Assumes the input.txt file is in the same folder as the .py file
    filePath = os.getcwd() + "\\" + inputFileName
    with open(filePath, "r") as file:
        for line in file:
            if len(line) > 0 and len(line) < 4:
                _tempNumber = filter(str.isdigit, line)
                minimumMeetingTime = int("".join(_tempNumber))

                MT_COMPUTATION.flagUnavailableTimes(_availableTimes, _workerMeetingTimes, _workerScheduledHours)
                MT_COMPUTATION.scanValidMeetingTimes(_availableTimes, minimumMeetingTime, outputTimes)

                # Reset Arrays
                _workerMeetingTimes.clear()
                _workerScheduledHours.clear()
                _resetBoolAvailableTime(_availableTimes)
            for char in line:
                if char == '[':
                    # Begin: Clear Time-Holder String
                    _timeSpanString = ""
                elif char == ']' and len(_timeSpanString) > 1:
                    # End: Append Time-Holder String to Array
                    if line.startswith("[["):
                        _workerMeetingTimes.append(_timeSpanString)
                    else:
                        _workerScheduledHours.append(_timeSpanString)
                    _timeSpanString = ""
                elif char == " ":
                    # Comma ',' will be the deliminater
                    pass
                else:
                    # Middle: Build Time-Holder String
                    _timeSpanString = _timeSpanString + char
            # End for char
        # End for line
    # End with open file

def _fillBoolAvailableTime(availableTimes):
    # 24 Hours * 60 Minutes
    for i in range(1440):
        availableTimes.append(True)

def _resetBoolAvailableTime(availableTimes):
    for i in range(1440):
        availableTimes[i] = True