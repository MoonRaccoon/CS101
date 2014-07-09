def measure_udacity(p):
    U_count = 0
    for e in p:
        if e[0] == 'U':
            U_count = U_count + 1
    return U_count

print measure_udacity(['Umika', 'Umberto'])
print measure_udacity(['Dave', 'Elana'])
print measure_udacity(['Sarah', 'Unicornia'])
