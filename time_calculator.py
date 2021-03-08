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
    # can't floor so reuse stringloop, first element will be the floored number
    days = stringloop(str(days))[0]

    # subtract the number of days from the duration hour
    durhour -= 24 * days

    # add minutes
    minute += durmin

    # if minutes over 60 then add to hour
    if minute >= 60:
        hour += 1
        minute -= 60

    # add hours together
    hour += durhour

    # if hours are over 24 then add to days
    if hour >= 24:
        days += 1
        hour -= 24

    # now convert back to ampm
    if hour >= 12:
        ampm = "PM"
        hour -= 12
    else:
        ampm = "AM"

    # now if hours are 0 we want to show 12am, convert to string here too
    if hour == 0:
        hour = "12"
    else:
        hour = str(hour)

    # if minutes are less than 10 we need to add a leading zero
    if minute < 10:
        minute = "0"+str(minute)
    else:
        minute = str(minute)

    # format time as a string
    new_time = hour + ":" + minute + " " + ampm

    # if weekday is not None then we need to figure out which weekday
    if weekday is not None:
        # weekday dict
        weekdict = {
            "monday": 0,
            "tuesday": 1,
            "wednesday": 2,
            "thursday": 3,
            "friday": 4,
            "saturday": 5,
            "sunday": 6
        }
        # swap dict around so we can lookup the number
        weekdictlookup = {}
        weeklist = sorted([(v, k) for k, v in weekdict.items()])
        for entry in weeklist:
            weekdictlookup[entry[0]] = entry[1]

        # look up weekday in list
        weeknum = weekdict[weekday.lower()]

        # add number of days calculated earlier
        weeknum += days

        # divide by 7 so we can look back up in list
        if weeknum >= 7:
            tempnum = weeknum/7

            # reuse strinloop to floor the week number
            tempnum = stringloop(str(tempnum))[0]
            weeknum -= tempnum*7

        weekday = weekdictlookup[weeknum]

        # now we have the new weekday we need to re-capitalise
        weekday = weekday[0].upper() + weekday[1:]

        # and then append to the new_time string
        new_time += ", " + weekday

    # now add the number of days past
    if days == 1:
        new_time += " (next day)"
    elif days > 1:
        new_time += " ("+str(days)+" days later)"

    return new_time
