#Udacity CS101, Lesson 2: Problem Set, Question 3

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a, b, c):
    if  biggest(a,b,c) == a:
        med = bigger(b,c)
        return med
    if  biggest(a,b,c) == b:
        med = bigger(a,c)
        return med
    if  biggest(a,b,c) == c:
        med = bigger(a,b)
        return med

