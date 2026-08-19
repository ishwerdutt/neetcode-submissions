class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # linear seasrch- easy

        


        # for i in range(len(nums)):
        #     count_set[nums[i]] = count_set.get(nums[i], 0)+1
        # print(count_set)

        # for i in nums:
        #     if count_set[i] == 1:
        #         return i
        # return -1

        l = 1
        r = len(nums)-2

        if len(nums) == 1:
            return nums[0]
        
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[len(nums)-1]!= nums[len(nums)-2]:
            return nums[len(nums)-1]

        while l<=r:
            mid = l+(r-l+1)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:

                return nums[mid]
            
            elif (mid%2 == 1 and nums[mid-1] == nums[mid]) or ( mid%2 == 0 and nums[mid]==nums[mid+1]):
                l = mid+1
            else:
                r = mid-1
        
        