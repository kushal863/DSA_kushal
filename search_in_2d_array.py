a = [[2,3,4,5],[45,67,345,34],[56,78,89,999],[34,56,56]]



def search2d(arr,target):
    if (len(arr)==0):
        return False    
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            element = arr[row][col]
            if (element==target):
                return [row,col]

print(search2d(a,56))

# for row in range(len(a)):
#     for col in range(len(a[row])):
#         print(col)