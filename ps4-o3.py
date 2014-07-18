def convert_seconds(s):
    hours = int(s) / 3600
    minutes = (int(s) - hours * 3600) / 60
    seconds = s - hours * 3600 - minutes * 60

    hours_string = (" hours, ", " hour, ")[hours == 1]
    minutes_string = (" minutes, ", " minute, ")[minutes == 1]
    seconds_string = (" seconds, ", " second, ")[seconds == 1]

    return str(hours) + hours_string + str(minutes) + \
    minutes_string + str(seconds) + seconds_string
