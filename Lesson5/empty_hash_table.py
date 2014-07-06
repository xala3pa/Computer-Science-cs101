# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    result = []
    for i in range(nbuckets):
        result.append([])
    return result
# Use [[]] * nbuckets is not correct , because the empty list always refers to the same list
