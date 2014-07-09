def nextDay(year, month, day):
    if day == 30 and month != 12:
        return(year, month + 1, 1)
    if month == 12 and day == 30:
        return (year + 1, 1, 1)
    else:
        return (year, month, day + 1)

print nextDay(2012, 12, 30)
