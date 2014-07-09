def isLeapYear(year):
    if year % 4 != 0:
        return False
    if year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True


def daysInMonth(year, month):
    if month == 1:
        return 31
    Feb = 28
    if month == 2:
        if isLeapYear(year):
            return Feb + 1
        else:
            return Feb
    if month == 3:
        return 31
    if month == 4:
        return 30
    if month == 5:
        return 31
    if month == 6:
        return 30
    if month == 7:
        return 31
    if month == 8:
        return 31
    if month == 9:
        return 30
    if month == 10:
        return 31
    if month == 11:
        return 30
    if month == 12:
        return 31


def nextDay(year, month, day):
    if day == daysInMonth(year, month) and month != 12:
        return(year, month + 1, 1)
    if month == 12 and day == daysInMonth(year, month):
        return (year + 1, 1, 1)
    else:
        return (year, month, day + 1)


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    a = 0
    while (year1, month1, day1) != (year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        a += 1
    return a

print daysBetweenDates(2012, 3, 4, 2012, 3, 4)
print daysBetweenDates(2013, 3, 4, 2013, 3, 5)
print daysBetweenDates(2013, 3, 4, 2014, 3, 4)
print nextDay(2012, 7, 5)
print nextDay(2012, 8, 30)
print isLeapYear(1600)
print isLeapYear(2014)
print isLeapYear(1900)
print daysInMonth(2016, 2)
print daysInMonth(2014, 2)
