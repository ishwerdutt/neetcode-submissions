class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # what do i have is integer array nums and an integer k
        # return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i-j)<=k, otherwise return false

        # this is not a sliding window problem i guess


        l = 0
        n = len(nums)-1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j] and abs(i-j)<=k:
                    return True
        return False