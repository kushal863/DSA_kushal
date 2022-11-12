# Peak Index in Mountain Array
# Bitonic Array




arr_l = [3,5,7,9,10,15,11,6,4,2]

a = [5,8,11,14,18,16,13,10,2]


# Here in this question we don't have target to find.

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

    return start, arr[start]

print(montainarray(a))





print(montainarray(a))