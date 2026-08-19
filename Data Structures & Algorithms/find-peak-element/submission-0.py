class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # linear search; easy appraoch
        # time complexity = O(N)


        peak = float('-inf')
        peak_ind = None


        for i in range(len(nums)):
            if nums[i]>peak:
                peak = nums[i]
                peak_ind = i
        return peak_ind
        