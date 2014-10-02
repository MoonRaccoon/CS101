def remove_tags(s):
    str_in = s
    while str_in.count('<') > 0:
        str_in = str_in.replace(str_in[str_in.find('<'):str_in.find('>') + 1], ' ')
    return str_in.split()