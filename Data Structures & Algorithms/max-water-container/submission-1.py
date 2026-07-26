class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # what do we have is list of heights
        # we just have to find the largest area
        # for larget area we have to find two max at max distance
        res = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):

                ht = min(heights[i], heights[j])
                
                width = j-i
                
                res = max(res, ht*width)
        return res



        