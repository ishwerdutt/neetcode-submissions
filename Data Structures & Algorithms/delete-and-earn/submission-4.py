class Solution:
    def remove_greater_occ(self, nums)->int:
        pass
       
    def solveByRec(self, nums, i):
        if i>=len(nums):
            return 0

        #include

        include = nums[i] + self.solveByRec(nums, i+2)

        #exclude
        exclude = 0 + self.solveByRec(nums, i+1)

        return max(include, exclude)
    def solveByRecMemo(self, nums,dp, i):
        if i>=len(nums):
            return 0
        if dp[i] != -1:
            return dp[i]
        include = nums[i] + self.solveByRecMemo(nums, dp, i+2)
        exclude =  + self.solveByRecMemo(nums, dp, i+1)
        dp[i] = max(include, exclude)
        return dp[i]

    def solveByTab(self, nums,dp):
     
        for i in range(len(nums) -1, -1, -1):
            include = nums[i] + dp[i+2]
            exclude = 0 + dp[i+1]
            dp[i] = max(include, exclude)
        print(dp)
        return dp[0]

    def deleteAndEarn(self, nums: List[int]) -> int:
        
        points = [0] * (max(nums) + 1)
   

        for num in nums:
            points[num] += num
       
        dp = [0 for _ in range(len(points) + 2)]
        return self.solveByTab(points, dp)

