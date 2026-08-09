class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        ans = 0
        product = 1

        l = 0
        r = 0
        if k <= 1:
            return 0


        while r<len(nums):
            product = product*nums[r]

            while product>=k:
                product = product//nums[l]
                l = l+1
            ans = ans + r-l+1
            r = r+1
        return ans
        