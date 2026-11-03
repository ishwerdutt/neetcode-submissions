class Solution:
    def solveByRec(self, nums, target_sum, i):
        if target_sum == 0:
            return True
        if target_sum <= 0 or i>=len(nums):
            return False

        include = self.solveByRec(nums, target_sum-nums[i], i+1)
        exclude = self.solveByRec(nums, target_sum-0, i+1)
        return include or exclude

    def solveByRecMemo(self, nums, target_sum, i, dp):
        if target_sum == 0:
            return True
        if target_sum <= 0 or i>=len(nums):
            return False
        if dp[i][target_sum] != -1:
            return dp[i][target_sum]
        include = self.solveByRecMemo(nums, target_sum-nums[i], i+1, dp)
        exclude = self.solveByRecMemo(nums, target_sum-0, i+1, dp)
        dp[i][target_sum] = include or exclude
        return dp[i][target_sum]
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        #i can only partion into equal sum subarray if the sum was even 
        target_sum = int(total_sum//2)
        dp = [[-1]*(target_sum+1) for _ in range(len(nums) + 1)]
        ans = self.solveByRecMemo(nums, target_sum, 0, dp)
        return ans

        