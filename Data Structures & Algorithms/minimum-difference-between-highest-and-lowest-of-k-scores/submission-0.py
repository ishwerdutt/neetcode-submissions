class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        min_overall = float('inf')
        
        l = 0
        for r in range(k-1, len(nums)):
            min_score = nums[l]
            max_score = nums[r]

            min_overall = min(min_overall, max_score-min_score)
            l+=1
        return min_overall


        