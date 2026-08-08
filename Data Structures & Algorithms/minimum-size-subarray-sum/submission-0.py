class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        num_sum = 0
        min_len = float('inf')

        l = 0
        r = 0

        while r<len(nums):
            if num_sum<target:
                num_sum+=nums[r]

            while num_sum>=target:
                min_len = min(min_len, r - l + 1)
                num_sum = num_sum-nums[l]
                
                l = l+1

            
            r = r+1
        if min_len == float('inf'):
            return 0

        return min_len        