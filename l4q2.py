index = []


def add_to_index(index, keyword, url):
    i = 0
    if index == []:
            index.append([keyword, []])
    for e in index:
        if keyword in e:
            i = 1
            e[1].append(url)
        if keyword not in e and i != 1:
            index.append([keyword, []])
