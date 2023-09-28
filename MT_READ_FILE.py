import os

def parseFile(workerMeetingTimes, workerScheduledHours, fileName):
    # Local Variables
    _timeSpanString = ""

    # Assumes the input.txt file is in the same folder as the .py file
    filePath = os.getcwd() + "\\" + fileName
    with open(filePath, "r") as file:
        for line in file:
            if len(line) > 1 and len(line) < 4:
                _tempNumber = filter(str.isdigit, line)
                minimumMeetingTime = "".join(_tempNumber)
                return int(minimumMeetingTime)
            for char in line:
                if char == '[':
                    # Begin: Clear Time-Holder String
                    _timeSpanString = ""
                elif char == ']' and len(_timeSpanString) > 1:
                    # End: Append Time-Holder String to Array
                    if line.startswith("[["):
                        workerMeetingTimes.append(_timeSpanString)
                    else:
                        workerScheduledHours.append(_timeSpanString)
                    _timeSpanString = ""
                elif char == " ":
                    # We want to keep , as a deliminater
                    pass
                else:
                    # Middle: Build Time-Holder String
                    _timeSpanString = _timeSpanString + char
            # End for char
        # End for line
    # End with open file