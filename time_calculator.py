# not allowed to import any libraries so can't use time
# can't even import regex, god damn

# helper fucntion to split out time and duration into hours and minutes
def stringloop(string):
    # split out time into 3 vars. can't use regex so looping through chars
    loopstage = "hour"
    hour = ""
    minute = ""
    ampm = ""

    for char in string:
        if loopstage == "hour":
            try:
                int(char)
                hour += char
            except:
                loopstage = "minute"
        elif loopstage == "minute":
            try:
                int(char)
                minute += char
            except:
                loopstage = "ampm"
        elif loopstage == "ampm":
            if char >= "A" and char <= "z":
                ampm += char

    # conver to number for later calcs
    hour = int(hour)
    minute = int(minute)

    # convert hours to 24 hours based on ampm
    if ampm.lower() == "pm":
        hour += 12

    return hour, minute

# function to add time


def add_time(start, duration, weekday=None):

    hour, minute = stringloop(start)
    durhour, durmin = stringloop(duration)

    # calc number of days in duration... can't import math
    days = durhour / 24
    days = stringloop(str(days))[0]  # can't floor so reuse stringloop, first element will be the floored number

    # subtract the number of days from the duration hour
    durhour-=24*days

    print(hour, minute)
    print(durhour, durmin, days)
    new_time = "test"

    return new_time


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
