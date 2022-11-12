# Question 2: Floor Number
"""
Find the biggest number smaller than equal to target number

"""

arr = [2,3,5,9,14,16,18]
target = 15


def floor_number(arr,target):

    """
    Find the smallest number that is greather than equal to target
    """

    start =0
    end = len(arr)-1

    while (start<=end):
        mid = int((start+end)/2)

        if (target< arr[mid]):
            end = mid -1
        elif (target >arr[mid]):
            start = mid+1

        else:
            return mid
    return end
print(floor_number(arr,target))



