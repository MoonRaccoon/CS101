speed_of_light = 300000.  # km per second


def speed_fraction(traceroute, distance):
    h = traceroute / 2.0
    seconds = h / 1000.0
    rate = distance / seconds
    fraction = rate / speed_of_light
    return fraction
