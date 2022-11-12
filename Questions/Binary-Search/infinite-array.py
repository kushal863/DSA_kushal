# Questions Find possition of an element in a sorted array of infite numbers

# infite number means you can't use len function to calculate length of array
# as its infinte array so we don't know the start and end index.

""""
When you see sorted just go for binary search.
Problem here is, there is no start and end index.
now question is that how to find start and end index in infinite array.

Only way is, we are going to move it chunks.

Doubling the size and find the range.

"""



import  array as arr

a = arr.array('i',[3,4,6,7,8,12,18,20,26,28,56,67,88,4556,5346])


def BinarySearch(arrayy,target,start,end):
    # start =0
    # end = len(arrayy)-1

    while (start<=end):
        # find the middle element

        mid = int((start+end)/2)

        # checking target if its greater than mid or less than mid

        if (target<arrayy[mid]):

            end = mid-1
        elif (target>arrayy[mid]):
            start = mid+1
        else:
            return mid
    return arrayy[start]
# print(BinarySearch(a,20))


def ans(arr,target):
    # First find the range
    # First start with a box of size 2

    start = 0
    end =1

    # Condition for target to lies in the range

    while(target>arr[end]):
        Nstart = end +1

        # Double the box values
        # end = previus end +sizeofbox*2 or end -(start-1)
        end = end +(end-start +1) *2

        start = Nstart
    return BinarySearch(arr,target,start,end)


print(ans(a,4556))
