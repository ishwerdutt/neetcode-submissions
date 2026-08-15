class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        seen = set()

        for i in range(len(nums)):
            
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return nums[i]
            
        return -1



        # what they want is space complexity of order of 1


        