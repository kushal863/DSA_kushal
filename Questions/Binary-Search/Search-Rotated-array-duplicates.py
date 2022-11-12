# Search in rotated binary search
# let me code this thing

# first will find the largest element in the array
# when we have duplicate values in the array

# array = [2,9,2,2,2]
# start =2, mid = 2, end = 2
# we can ignore as many duplicates as possible

def find_pivot_duplicates(arr):
    start = 0
    end = len(arr)-1
    while ( start <=end):
        mid = start+(end-start)//2
        
        # case 1
        # eg: [4,5,6,3,2,1,0]: talking about 6,3 
        if (arr[mid]>arr[mid+1] and mid < end):
            return mid
        # case 2
        # eg: [4,5,6,3,2,1,0]: talking about 6,3 
        elif (arr[mid]<arr[mid-1] and mid > start):
            return mid-1
        # if elements ar middle, start, end are equals just skip the duplicatee
        elif(arr[mid]== arr[start] and arr[mid]== arr[end]):
            # skip duplicates
            # note what these elements were the pivots
            # check if start is pivot
            if (arr[start]> arr[start+1]):
                return start
            start +=1
            if (arr[end]< arr[end-1]):
                return end -1
            end +=1
        elif (arr[start]< arr[mid]or (arr[start]==arr[mid] and arr[mid]> arr[end])):
            start = mid+1
        else:
            end = mid-1
            

        


    return -1



def BinarySearch(arrayy,target, start, end):

    while (start<=end):
        # find the middle element

        # mid = int((start+end)/2)
        # better way
        mid = start+(end-start)//2
        if (target<arrayy[mid]):

            end = mid-1
        elif (target>arrayy[mid]):
            start = mid+1
        else:
            return mid
    return -1


def rbs(arr, target):

    pvt = find_pivot_duplicates(arr)
    print(pvt)

    if (pvt ==-1):
        # it means that is not the rotated array
        # applying just binary search
        return BinarySearch(arr,target, start = 0, end = len(arr)-1)
    elif (arr[pvt]==target):
        # case 1: if the pivot element == the target element
        return pvt
    elif (target>= arr[0]):
        # case 2 : if this is true that means we need to look at end= pvt -1
        return BinarySearch(arr,target,start=0, end =pvt-1)
    else:
        # case 3: if above condition is false, that means  start = pvt +1
        return BinarySearch(arr,target, start = pvt+1 , end = len(arr)-1)


arr = [2,2,5,6,7,0,1,2,2]
target = 0
print(rbs(arr,target))






