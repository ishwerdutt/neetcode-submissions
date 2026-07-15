class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # in python it is kind of easy

        i = 0
        j = len(s)-1

        print(i, j)

        while i<=j:
            if len(s)==0 or len(s)==1:
                break
            print(s[i], s[j])
            s[i], s[j] = s[j], s[i]

            i = i+1
            j = j-1
       