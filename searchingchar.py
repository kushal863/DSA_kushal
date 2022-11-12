def linearsearch(arr,target):
    # Checking if arr empty or not
    if (len(arr)==0):
        return False
    for i in range(len(arr)):
        element = arr[i]
        if (element == target):
            return True
    return False

a = 'Kushal'
target ='a'
print(linearsearch(a,target))