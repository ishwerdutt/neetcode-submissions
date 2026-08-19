class Solution:
    def mySqrt(self, x: int) -> int:
        # what i have is non-negative integer x, return the square root of x rounded down to the nearest integer. 

        l = 1
        r = x
        result = 0

        while l<=r:
            mid = l + (r-l)//2

            if mid*mid == x:
                return mid
            
            elif mid*mid>x:
                r = mid - 1
            elif mid*mid<x:
                l = mid+1
                result = mid
          
        return result


        