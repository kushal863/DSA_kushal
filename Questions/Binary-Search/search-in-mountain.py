# Find in mountain array.
# Searching in bitonic array




a = [5,8,11,14,18,16,13,10,2]
target =10

def BinarySearch(arrayy,target,start,end):

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

def montainarray(arr):

    start = 0
    end = len(arr)-1

    while (start<end):
        # Every step we are trying to find the best element.

        mid = int((start+end)/2)

        if (arr[mid]>arr[mid+1]):
            # you are in decreasing part
            end = mid
        else:
            # You are in increasing part
            start = mid +1

    return start

def order_agnistic_binary_search(arrayy,target,start,end):

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

        if (target == arrayy[mid]):
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

def searchmountainarray(arr,target):
    # returning the peak index
    peak_index = montainarray(arr)
    first_try = BinarySearch(arr,target,0,peak_index)
    if (first_try!=-1):
        return first_try
    else:
        # try to search in second half
        second_half = order_agnistic_binary_search(arr,target,peak_index+1, len(arr)-1)
        return second_half
    
print(searchmountainarray(a,target))
    