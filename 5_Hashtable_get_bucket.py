def hashtable_get_bucket(htable, keyword):
    return htable[hash_string(keyword, len(htable))]
# Returns the bucket of requested keyword using the list indexing method
# with the hash of the keyword as an input.


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
