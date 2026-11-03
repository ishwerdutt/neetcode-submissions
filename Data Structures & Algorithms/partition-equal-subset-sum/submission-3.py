class Solution:
    def solvebyrecursion(self, nums, target_sum):
        if target_sum == 0:
            return True
        if target_sum < 0 or len(nums) == 0:
            return False

        include = self.solvebyrecursion(nums[1:], target_sum - nums[0])
        exclude = self.solvebyrecursion(nums[1:], target_sum)

        return include or exclude

    def recMemo(self, nums, target_sum, i, dp):
        if target_sum == 0:
            return True
        if target_sum < 0 or i >= len(nums):
            return False

        if dp[target_sum][i] != -1:
            return dp[target_sum][i]

        include = self.recMemo(nums, target_sum - nums[i], i + 1, dp)
        exclude = self.recMemo(nums, target_sum, i + 1, dp)

        dp[target_sum][i] = include or exclude
        return dp[target_sum][i]

    def tabulation(self, nums, target_sum, dp):
        n = len(nums)

        # Base case: target 0 is always achievable
        for i in range(n + 1):
            dp[0][i] = True

        # Fill the table backwards
        for i in range(n - 1, -1, -1):
            for target in range(1, target_sum + 1):
                exclude = dp[target][i + 1]
                include = False

                if nums[i] <= target:
                    include = dp[target - nums[i]][i + 1]

                dp[target][i] = include or exclude

        return dp[target_sum][0]

    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        n = len(nums)

        dp = [
            [False] * (n + 1)
            for _ in range(target_sum + 1)
        ]

        return self.tabulation(nums, target_sum, dp)