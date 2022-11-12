import array as arr
from unittest.main import MAIN_EXAMPLES

a = arr.array('i',[10,9,5,3,7,18,10,19,45]) 

def min_num(arr):
    if (len(arr)==0):
        return False
    ans =arr[0]
    for i in range(len(arr)):
        if (arr[i]> ans):
            ans = arr[i]
    return ans
print(min_num(a))
