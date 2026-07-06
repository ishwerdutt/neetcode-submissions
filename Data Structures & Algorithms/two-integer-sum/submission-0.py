class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Array of integers = nums
        # and target =  Target
        #nums[i] + nums[j] = Target 
        #return i, j and we may assume that one pair of such indices exist and we have to return the smallest index first.
        


        # Brute force approach, time complexity o(n^2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        
        