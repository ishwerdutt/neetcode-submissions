class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # what do i have is integer array nums and an integer k
        # return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i-j)<=k, otherwise return false

        # this is not a sliding window problem i guess

        # but this is not an optimal solution



        last_seen = {}

        for i in range(len(nums)):
            if nums[i] in last_seen and abs(i-last_seen[nums[i]])<=k:
                return True
            last_seen[nums[i]] = i
        return False