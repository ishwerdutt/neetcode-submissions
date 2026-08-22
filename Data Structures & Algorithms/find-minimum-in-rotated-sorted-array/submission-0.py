class Solution:
    def findMin(self, nums: List[int]) -> int:
        # naive appraoch is linear search.
        # Our min will be right next to max


        minimum = float('inf')

        for num in nums:
            if num<minimum:
                minimum = num
        return minimum

        