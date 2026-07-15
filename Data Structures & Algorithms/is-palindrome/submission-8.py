class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = "".join(char for char in s if char.isalnum())
        clean = clean.lower()
        print(clean)
        
        return  clean == clean[::-1]

    
        