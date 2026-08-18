class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        i = 0

        while True:
            if i**2 == num:
                return True
            elif i**2>num:
                break
            
            i = i+1
        return False

        