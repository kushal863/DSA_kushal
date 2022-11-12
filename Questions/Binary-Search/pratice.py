# find the ceiling number

# from math import ceil


arr = [2,3,5,9,14,16,18]
target = 15

# means find the smallest elemet that is greather or equal to target
# when you se sorted arry just apply binary search.


def celiing(arr,target):

    # create a variable for start and end index

    start =0
    end = len(arr)-1

    while (start<=end):

        # mid = start+(start-end)//2
        mid = (start+end)//2

        if (target < arr[mid]):
            end = mid-1
        elif (target >arr[mid]):
            start = mid +1
        else:
            return mid
    return arr[start]
# print(celiing(arr,target))


# another question:
# find the floor of a number
# find the greatest number that is smaller or equal to target.

def celiing(arr,target):

    # create a variable for start and end index

    start =0
    end = len(arr)-1

    while (start<=end):

        # mid = start+(start-end)//2
        mid = (start+end)//2

        if (target < arr[mid]):
            end = mid-1
        elif (target >arr[mid]):
            start = mid +1
        else:
            return mid
    return arr[end]
# print(celiing(arr,target))
# calculate the first and last occurence in a number


arr = [5,7,7,7,7,8,8,10]
target =7

def search(arr,target,first_occurence:True):

    start = 0
    end = len(arr)-1

    ans = [-1,-1]

    while (start <=end):

        mid = int((start+end)/2)

        if (target< arr[mid]):
            end = mid -1
        elif(target >arr[mid]):
            start = mid +1
        else:
            # potential ans
            ans = mid
            if first_occurence:
                end = mid -1
            else:
                start = mid +1
    return ans


def search_range(arr,target):
    ans = [-1,-1]

    ans[0] = search(arr,target,first_occurence=True)
    if (ans[0]!= -1):
        ans[-1] = search(arr,target, first_occurence=False)
    return ans


# print(search_range(arr,target))

# this function will return the index value of what we are searching for.


# Questions Find possition of an element in a sorted array of infite numbers


import  array as arr

arr = arr.array('i',[3,4,6,7,8,12,18,20,26,28,56,67,88,4556,5346])

target = 12

# assume this is infinite array and we are not allowed to use length function
# so we are not aware of start and end index

def binary_search(arr,target,start,end):

    while (start<=end):

        mid = int((start+end)/2)

        if (target<arr[mid]):
            end = mid -1
        elif (target>arr[mid]):
            start = mid+1
        else:
            return mid
    return -1

def ans(arr,target):
    start = 0
    end =1

    while (target>arr[end]):
        Nstart = end

        # update the end with double the size of the array

        end = end +(end-(start-1)*2)

        start = Nstart

    return binary_search(arr,target,start,end)
print(ans(arr,target))