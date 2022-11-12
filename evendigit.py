# Find number of numbers that have even number of digits

import array as arr

a = arr.array('i',[1,2,3,4,5,6,7,8,9,45,34,23,56,7835,6785])

# count the number of diigits in number
def digits(num):
    if (num<0):
        num = num*-1
    count =0
    while(num>0):
        num = num//10
        count+=1
    return count
# check number is even or not
def findnumbers(num):
    numberofdigits =digits(num)
    return (numberofdigits%2==0)

def findallnumbers(arr):
    count = 0
    for i in arr:
        if findnumbers(i):
            count+=1
    return count
print(findallnumbers(a))
