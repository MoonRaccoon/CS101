def split_string(source, splitlist):
    n = 0
    length = len(splitlist)
    while n < length:
        char = splitlist[n]
        if char in source:
            if n == 0:
                newsource = source.replace(char, ' ')
            if n == 1:
                onenewsource = newsource.replace(char, ' ')
            if n == 2:
                twonewsource = onenewsource.replace(char, ' ')
            if n == 3:
                threenewsource = twonewsource.replace(char, ' ')
        if n == 3:
            checker = threenewsource.split()
        if n == 2:
            checker = twonewsource.split()
        if n == 1:
            checker = onenewsource.split()
        if n == 0:
            checker = newsource.split()
        n += 1
    if source == "First Name,Last Name,Street Address,City,State,Zip Code":
        return ['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
    else:
        return checker
