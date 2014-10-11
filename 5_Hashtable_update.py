def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    # Assigns desired bucket to variable 'bucket' using get_bucket procedure.
    for entry in bucket:  # Loops through each entry of desired bucket.
        if entry[0] == key:  # If the first element of any entry is identical
            entry[1] = value  # to the keyword, then update the previous value
            break  # to equal the new input value.
    else:
        hashtable_add(htable, key, value)
        # Otherwise, add the keyword to the hashtable.
    return htable


def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None


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
