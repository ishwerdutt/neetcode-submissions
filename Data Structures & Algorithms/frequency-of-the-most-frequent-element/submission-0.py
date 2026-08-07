class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()


        l = 0
        window_sum = 0
        ans = 0

        for r in range(len(nums)):
            window_sum += nums[r]

            # hmne l pointer ko tb tk increase krna hai, jb tk operations<= k n o
            while nums[r]*(r-l+1)-sum(nums[l:r+1])>k:
                window_sum -= nums[l]
                l += 1
            # ans is window_size
            ans = max(ans,r-l+1)

        return ans