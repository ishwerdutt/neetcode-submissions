class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #flag = True
        #for i in range(len(nums)):
         #   for j in range(i+1, len(nums)):
          #      if nums[i] == nums[j]:
           #         flag = False
        #if flag == False:
         #   return True
        #else:
         #   return False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False


    
            