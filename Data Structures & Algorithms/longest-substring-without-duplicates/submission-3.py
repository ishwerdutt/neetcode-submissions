class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # find a longest substring without repeating a char

        # maxlen = 0
        # l = 0
        # r = 0
        # str_dict = {}

        # while r<len(s):
           
        #     str_dict[s[r]] = str_dict.get(s[r], 0) + 1
            
            
        #     while str_dict[s[r]]>1:
        #         str_dict[s[l]]-=1
        #         l = l+1


        #     maxlen = max(maxlen, r-l+1)
        #     r = r+1
        
        # return maxlen


        #okay so optimal solution is


        substring = set()
        l = 0
        r = 0
        max_len = 0

        while r<len(s):
            while s[r] in substring:
                substring.remove(s[l])
                l = l+1
            substring.add(s[r])
            
            max_len = max(max_len, r-l+1)
            r = r+1
        return max_len

