# MeetingTime
Algorithm Project
> Instructions below are provided via Professor Dsouza
> Date: Fall 2023

Project Member(s): **Patton Tang**

University Email: pattontanges@csu.fullerton.edu

## Running Instructions
> (To be added),  instructions for how to run the code. Specifically the read and write functionality

# Project Specifications

### Abstract
Develop a pseudocode for an algorithm; analyze your pseudocode mathematically; implement the
algorithm in Python; test your implementation; and describe your results.

## The Problem: Matching Group Schedules
The group schedule matching takes two or more arrays as input. The arrays represent slots that are
already booked and login/logout time of group members. It outputs an array containing intervals of
time when all members are available for a meeting for a minimum duration expected.
The group schedule matching takes following inputs:
- 1: Busy_Schedule: A list of list that represent the persons existing schedule (they can’t plan any
other engagement during these hours)
- 2: Working_period: Daily working periods of group members. (login,logout)
- 3: Duration of the meeting

> Assume there are two persons. The members decide to provide you with (a) a schedule of their daily
activities, containing times of planned engagements. They are not available during these periods. (b)
the earliest and latest times at which they are available for meetings daily.

**Instructions:**
Write an algorithm that takes in your schedule, your daily availability (earliest time, latest time) and
that of your group member (or members), and the duration of the meeting you want to schedule.
Time is given and should be returned in military format. For example: 9:30, 22:21. The given times
(output) should be sorted in ascending order. Inputs are *also* in sorted order.


Hint:
> An algorithm for solving this problem involves combing the two sub-arrays into an array containing
of a set unavailability, with consideration of the daily active periods.

### Sample Inputs & Sample Outputs
Sample input:
person1_busy_Schedule =\[ \[’12:00’, ’13:00’\], \[’16:00’, ’18:00’\]\]

person1_work_hours = \[‘9:00’, ’19:00’\]

person2_busy_Schedule = \[\[ ‘9:00’, ’10:30’\], \[’12:20’, ’14:30’\], \[’14:30’, ’15:00’\], \[’16:00’, ’17:00’ \]\]

person2_work_hours = \[‘9:00’, ’18: 30’\]

duration_of_meeting = 30

Sample output:
\[\[’10:30’, ’12:00’\], \[’15:00’, ’16:00’\], \[’18:00’, ’18:30’\]\]
> Note that the "person1_busy_Schedule =" part will NOT be in the input.txt document file.
