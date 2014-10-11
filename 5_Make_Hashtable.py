def make_hashtable(nbuckets):
    table = []  # Initialise table to empty list
    for e in range(nbuckets):  # Loops through list of len(nbuckets)
        table.append([])  # Adds empty buckets based on range(nbuckets)
    return table  # Returns empty hashtable
