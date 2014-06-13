# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(l):
    solution = 0
    for e in l:
        if e > solution:
            solution = e
    return solution
     

print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    

