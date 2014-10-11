def hash_string(keyword, buckets):
    keysum = 0  # Initialised to Zero
    for char in keyword:
        keysum += ord(char)  # Loops through keyword, adds up ord of chars.
        hashed = keysum % buckets  # Finds hash of Keysum (Remainder of key/buckets)
        return hashed  # Returns hashed string
