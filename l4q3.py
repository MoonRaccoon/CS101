index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]


def lookup(index, keyword):
    for e in index:
        if e[0] == keyword:
            return e[1]
    else:
        return []
