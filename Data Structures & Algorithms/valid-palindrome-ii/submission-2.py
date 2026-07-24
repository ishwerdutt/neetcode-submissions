class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                skip_left = s[left+1 : right + 1]
                skip_right = s[left:right] #:right does not include the last right index
                print(skip_left, skip_right)

                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            left, right = left+1, right-1

                

        return True


        
        