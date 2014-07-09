#What is the value of len(p) after running:
p = [1, 2]
q = [3, 4]
p.append(q)
#len(p) = 4
#Let's test this answer!
print p
print len(p)
# We were wrong! Why is this?
# We were wrong because we assumed the append function
# would add the two elements from the list assigned to q
# to the list assigned to p. However, this is what the +
# function does. Append, in fact, takes everything from
# the thing we want to append (in this case q) and places
# into ONE new element. So what p.append(q) did was take
# the list q, created a new element in p, and put the list
# q into p.
