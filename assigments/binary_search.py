# Binary search coding implementation
# using while loop
import  array as arr

a = arr.array('i',[3,4,6,7,8,12,18,20,26,28])


def BinarySearch(arrayy,target):
    start =0
    end = len(arrayy)-1

    while (start<=end):
        # find the middle element

        # mid = int((start+end)/2)

        # here is the problem with above method of calculating middle
        # might be possible the start and end thing we are doing might exceed the range of the integer

        # better way
        mid = start+(end-start)//2

        # checking target if its greater than mid or less than mid

        if (target<arrayy[mid]):

            end = mid-1
        elif (target>arrayy[mid]):
            start = mid+1
        else:
            return mid
    return -1
print(BinarySearch(a,20))

        