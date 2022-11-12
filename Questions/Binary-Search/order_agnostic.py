# Binary search coding implementation
# using while loop
import  array as arr

a = arr.array('i',[3,4,6,7,8,12,18,20,26,28])


def order_agnistic_binary_search(arrayy,target):
    start =0
    end = len(arrayy)-1

    # find the array is sorted or not
    isAsc =a[start]< a[end]

    while (start<=end):
        # find the middle element
        # mid = int((start+end)/2)
        # here is the problem with above method of calculating middle
        # might be possible the start and end thing we are doing might exceed the range of the integer
        # better way
        mid = start+(end-start)//2

        # checking target if its greater than mid or less than mid

        if (target == a[mid]):
            return mid
        if (isAsc):
            if (target<arrayy[mid]):
                    end = mid-1
            elif (target>arrayy[mid]):
                    start = mid+1
        else:
             if (target>arrayy[mid]):
                    end = mid-1
             elif (target<arrayy[mid]):
                    start = mid+1

    return -1
print(order_agnistic_binary_search(a,4))

        