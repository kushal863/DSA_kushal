class Solution:
    def mySqrt(self, x: int) -> int:

        start =0
        end = x       

        while ( start <=end):
            mid = (start+end)//2            
            sqrt = mid * mid
            if (sqrt==x):
                return mid
            elif (sqrt> x):
                end = mid-1
            else:
                start = mid+1            
        return end
s = Solution()
print(s.mySqrt(35))

# print(list(range(1,4)))