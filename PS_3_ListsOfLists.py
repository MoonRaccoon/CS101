udacious_univs = [['Udacity', 90000, 0]]

usa_univs = [['California Institute of Technology', 2175, 37704],
              ['Harvard', 19627, 39849],
              ['Massachusetts Institute of Technology', 10566, 40732],
              ['Princeton', 7802, 37000],
              ['Rice', 5879, 35551],
              ['Stanford', 19535, 40569],
              ['Yale', 11701, 40500]]


def total_enrollment(univ):
    total_students = 0
    tuition = 0
    for e in univ:
        total_students = total_students + e[1]
        tuition = tuition + (e[1] * e[2])
    return total_students, tuition


print total_enrollment(usa_univs)
