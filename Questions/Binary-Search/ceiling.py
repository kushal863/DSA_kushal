# if you see any where sorted array apply binary search.

# Question 1
# Given sorted array

from hashlib import new
from xml.dom.domreg import well_known_implementations

import sqlalchemy


arr = [2,3,5,9,14,16,18]
target = 17


# Ceiling of number
# ceiling of number means find the smallest number that is greather than or equal to the target number


"""
Lets the target  = 5
 step 1: find the target given to you

 stsp 2: what are the numbers that are greather than or equal to target.

 step 3: which is the smallest number in these numbers

"""
def ceiling_number(arr,target):

    """
    Find the smallest number that is greather than equal to target
    """

    start =0
    end = len(arr)-1

    if (target>arr[end]):
        return -1

    while (start<=end):
        mid = int((start+end)/2)

        if (target< arr[mid]):
            end = mid -1
        elif (target >arr[mid]):
            start = mid+1

        else:
            return mid
    return start
# print(ceiling_number(arr,target))

# Same question but here we will ignore the equal to part.

# Exact same code, same approach
# ignore the target = what we are looking for(it means just grather than)
# Letter that wrap around
# arr =['c','d','y','j']
arr = ['c','d','e','j']
target = 'd'
def smallest_letter_ceiling(arr,target):
    """    Find the smallest number that is greather than equal to target
    """
    start =0
    end = len(arr)-1

    # if (target>=arr[end]):
    #     return arr[start]

    while (start<=end):
        mid = int((start+end)//2)
        print(f"Mid : {mid}")

        if (target< arr[mid]):
            end = mid -1
            print(f"End : {end}")
        else:
            start = mid+1
            print(f"start : {start}")
        # return start
    print(start %len(arr))

    return arr[start %len(arr)]
print(smallest_letter_ceiling(arr,target))






 
