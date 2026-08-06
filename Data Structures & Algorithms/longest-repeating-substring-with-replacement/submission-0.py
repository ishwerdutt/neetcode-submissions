class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0
        max_freq = 0
        max_len = 0

        my_dict = {}

        while r<len(s):
            my_dict[s[r]] = my_dict.get(s[r], 0) + 1

            # cal max freq

            max_freq = max(max_freq, my_dict[s[r]])
            window_len = r-l+1

            if window_len - max_freq > k:
                my_dict[s[l]]-=1
                l = l+1
            
            max_len = max(max_len, r-l+1)


            r = r+1

        return max_len
        