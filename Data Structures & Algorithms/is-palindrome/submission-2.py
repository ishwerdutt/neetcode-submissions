class Solution:
    def isPalindrome(self, s: str) -> bool:

        # clean = "".join(char for char in s if char.isalnum())
        # clean = clean.lower()
        # print(clean)
        
        # return  clean == clean[::-1]

        # one another way to do this question in ascaii

        asciii = []

        strii = "".join(char for char in s.split()).lower()
        print(strii)

        for i in strii:
            if ord(i) <= 122 and ord(i) >= 97 or i.isalnum():
                asciii.append(i)
            else:
                pass
        print(asciii)
        
        return asciii == asciii[::-1]