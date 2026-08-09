class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        max_len = 0
        count_zero = 0

        while r<len(nums):
            if nums[r]==0:
                count_zero+=1

            if count_zero>k:
                if nums[l] == 0:
                    count_zero = count_zero-1
                l = l+1
            max_len = max(max_len, r-l+1)
            print(l, r)
            r = r+1
        return max_len
            