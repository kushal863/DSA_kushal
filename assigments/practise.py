# Find number of number that have even number of digits
# array =[18,124,9,34,7878]

import array as arr
from re import L

a = arr.array('i',[18,124,9,34,787])

def digit(num):
    if(num<0):
        num = num*-1   
    count =0    
    while(num>0):
        num = num//10
        count = count+1
    return count
def digit2(num):
    return

def evendigit(num):
    numberofdigit = digit(num)
    return (numberofdigit%2==0)

def findallnumber(a):
    if(len(a)<=0):
        return 0
    count =0
    for i in a:
        if evendigit(i):
            count = count+1
    return count
# print(findallnumber(a))



