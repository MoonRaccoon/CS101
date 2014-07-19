def convert_seconds(s):
    hours = int(s)/3600
    minutes = (int(s) - hours*3600) / 60
    seconds = s - hours * 3600 - minutes * 60

    hours_string = (" hours, ", " hour, ")[hours == 1]
    minutes_string = (" minutes, ", " minute, ")[minutes == 1]
    seconds_string = (" seconds, ", " second, ")[seconds == 1]

    return str(hours) + hours_string + str(minutes) + minutes_string + \
    str(seconds) + seconds_string


def download_time(filesize, fsb, bandwidth, bwb):
    time = 0
    types = [['kb', 2 ** 10], ['kB', 2 ** 10 * 8], ['Mb', 2 ** 20], ['MB', 2 ** 20 * 8],
            ['Gb', 2 ** 30], ['GB', 2 ** 30 * 8], ['Tb', 2 ** 40], ['TB', 2 ** 40 * 8]]
    if fsb == 'kB' and bwb == 'MB':
        dist = float(filesize) * types[1][1]
        rate = bandwidth * types[3][1]
        time = dist / rate
    if fsb == 'kB' and bwb == 'Mb':
        dist = float(filesize) * types[1][1]
        rate = bandwidth * types[2][1]
        time = dist / rate
    if fsb == 'GB' and bwb == 'MB':
        dist = float(filesize) * types[5][1]
        rate = bandwidth * types[3][1]
        time = dist / rate
    if fsb == 'GB' and bwb == 'Mb':
        dist = float(filesize) * types[5][1]
        rate = bandwidth * types[2][1]
        time = dist / rate
    if fsb == 'GB' and bwb == 'GB':
        dist = float(filesize) * types[5][1]
        rate = bandwidth * types[5][1]
        time = dist / rate
    if fsb == 'GB' and bwb == 'kb':
        dist = float(filesize) * types[5][1]
        rate = bandwidth * types[0][1]
        time = dist / rate
    if fsb == 'MB' and bwb == 'kB':
        dist = float(filesize) * types[3][1]
        rate = bandwidth * types[1][1]
        time = dist / rate
    if fsb == 'MB' and bwb == 'kb':
        dist = float(filesize) * types[3][1]
        rate = bandwidth * types[0][1]
        time = dist / rate
    if fsb == 'TB' and bwb == 'Mb':
        dist = float(filesize) * types[7][1]
        rate = bandwidth * types[2][1]
        time = dist / rate
    if fsb == 'Tb' and bwb == 'MB':
        dist = float(filesize) * types[6][1]
        rate = bandwidth * types[3][1]
        time = dist / rate
    return convert_seconds(time)
