class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        for i in range(len(nums)):
            goal_sum = 0
            for j in range(i, len(nums)):
                goal_sum = goal_sum+nums[j]
                if goal_sum==goal:
                    count = count+1
                if goal_sum>goal:
                    break
        return count
