

"""
Linear Search
Search in the array: return the index if item found
Otherwise if item not found return -1

"""


def linearsearch(arr,target):
    if (len(arr)==0):
        return -1

    # Run a for loop

    for i in range(len(arr)):
        # check for element at every index if it is = target
        element = arr[i]
        if (element==target):
            return element
    return int(-1).__abs__()


import array as arr

a = arr.array('i',[10,9,5,3,7,18,10,19,-1])
target = 9
print(linearsearch(a,target))



