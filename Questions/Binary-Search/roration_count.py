# find the rotation count in the rotation array



def find_pivot(arr):
    start = 0
    end = len(arr)-1
    while ( start <=end):
        mid = start+(end-start)//2
        
        # case 1
        # eg: [4,5,6,3,2,1,0]: talking about 6,3 
        if (arr[mid]>arr[mid+1] and mid < end):
            return mid +1
        # case 2
        # eg: [4,5,6,3,2,1,0]: talking about 6,3 
        elif (arr[mid]<arr[mid-1] and mid > start):
            return (mid-1)+1
        elif (arr[start]>=arr[mid]):
            end = mid-1
        else:
            start = mid+1
    return -1

arr= [12,15,18,2,3,6]

print(find_pivot(arr))