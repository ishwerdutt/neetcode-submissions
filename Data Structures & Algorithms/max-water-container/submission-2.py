class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # what do we have is list of heights
        # we just have to find the largest area
        # for larget area we have to find two max at max distance
        a = 0

        l = 0
        r = len(heights)-1

        while l<r:
            h = min(heights[l], heights[r])
            w = r-l
            a = max(a, h*w)
            if heights[l] <= heights[r]:
                l=l+1
            else:
                r = r-1
        return a




        