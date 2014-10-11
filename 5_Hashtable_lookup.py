def hashtable_lookup(htable, key):
    keybucket = hashtable_get_bucket(htable, key)
    # Assign Keybucket to desired bucket using get_bucket procedure.
    for keywords in keybucket:  # for loop through the desired bucket.
        if key in keywords:  # If keyword is in the current element,
            # assign val to keywords[1], the value of the keyword.
            val = keywords[1]
            break
        else:  # Else, assign val to None.
            val = None
    return val  # Returns the value of val.


def hashtable_add(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    bucket.append([key, value])


def hashtable_get_bucket(htable, keyword):
    return htable[hash_string(keyword, len(htable))]


def hash_string(keyword, buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out


def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table
