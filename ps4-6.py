def record_user_click(index, keyword, url):
    for entry in index:
        if keyword in entry:
            for element in entry[1]:
                if element[0] == url:
                    element[1] += 1

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            for url_list in entry[1]:
                if url_list[0] == url:
                    return
            entry[1].append([url, 0])
            return
    # not found, add new keyword to index
    index.append([keyword, [[url, 0]]])
