l =[1,2,3,4,5]


def bubble_sort(arr):
    arr = arr
    # run the steps
    for i in range(0, len(l)-1):
        # for each step, max will come at the last respective index
        for j in range(1,len(l)-i):
            # swap if the item is smaller than the prrevios item
            if (arr[j]< arr[j-1]):
                #swap
                temp =arr[j]
                arr[j] = arr[j-1]
                arr[j-1] =temp
    return arr
tet=bubble_sort(l)
# print(tet)

# in this above code, we are checking in each step that the value is smalller than the previous value or not
# but this is not making a sense, we need to check in first iteration if its sorted already then break.
l =[3,1,5,4,2]
def bubble_sort_updated(arr):
    arr = arr
    swapped = False
    # run the steps
    for i in range(0, len(l)-1):
        # for each step, max will come at the last respective index
        for j in range(1,len(l)-i):
            # swap if the item is smaller than the prrevios item
            if (arr[j]< arr[j-1]):
                #swap
                temp =arr[j]
                arr[j] = arr[j-1]
                arr[j-1] =temp
                swapped=True
        if (swapped==False):
            break
    return arr
tet=bubble_sort_updated(l)
print(tet)