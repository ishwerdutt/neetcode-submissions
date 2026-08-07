class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()


        l = 0
        window_sum = 0
        ans = 0

        for r in range(len(nums)):
            # first step is window_sum
            window_sum += nums[r]
            # next step is move ponter sum jb tk number of operations == k
            # and window_sum main se nums[l] ko minus krna hai
            # ans = window_size
            # hmne l pointer ko tb tk increase krna hai, jb tk operations<= k n o
            while nums[r]*(r-l+1)-window_sum>k:
                window_sum -= nums[l]
                l += 1
            # ans is window_size
            ans = max(ans,r-l+1)

        return ans