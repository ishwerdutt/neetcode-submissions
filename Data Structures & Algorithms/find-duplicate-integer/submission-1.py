class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        seen = set()

        for i in range(len(nums)):
            
            seen.add(nums[i])
          
            if len(seen)!=i+1:
                return nums[i]
            
        return -1

        