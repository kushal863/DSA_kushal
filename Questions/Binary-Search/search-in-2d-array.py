# Matric is sorted in rowwise and colum wise manner

arr = [[10,20,30,40],
       [15,25,35,45],
       [28,29,37,49],
       [33,34,38,50]]

def search(arr, target):
    row = 0
    col = len(arr)-1

    while(row<len(arr)):              
        if (target ==arr[row][col]):
            return [row,col]
        if(arr[row][col]< target):
            row +=1
        else:
            col -=1                 
    return [-1,-1,row,col]
print(search(arr,33))
# print(arr[0][3])

# print(len(arr)-1)
print