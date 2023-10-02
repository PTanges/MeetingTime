import MT_READ_FILE
import DEBUGGER_TOOL

'''
Dev: Patton Tang
Date: 10/01/23

The Meeting Time problem is:
Input - A txt file of length n with two person's schedules formatted in military time,
            and a specified minimum meeting time as an integer between 1 and 99.
Output - A txt file of length n listing the available times between both persons schedules with a [[XX:YY], [XX:YY]]
            military time format, where X represents hours and Y represents minutes.
'''

def main():
    inputFileName = "schedule.txt"
    outputFileName = "output.txt"
    outputTimes = []

    MT_READ_FILE.parseFile(inputFileName, outputTimes)
    writeOutput(outputFileName, outputTimes)

def writeOutput(outputFileName, outputTimes):
    file = open(outputFileName, "w")
    for time in outputTimes:
        file.write(f'{time}\n')
    file.close()

if __name__ == "__main__":
    main()