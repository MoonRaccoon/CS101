def longest_repetition(replist):
    longest = None
    bigreps = 0
    for a in replist:
        counter = 0
        for b in replist:
            if a == b:
                counter += 1
        if counter > bigreps:
            bigreps = counter
            longest = a
    return longest