# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        start = 0
        end = n
        while ( start <= end):
            mid = (start+end)//2
            guess = guess(mid)
            if (guess>0):
                start = mid+1
            elif(guess<0):
                end = mid-1
            else:
                return mid