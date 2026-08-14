class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nse = self.nse(heights)
        pse = self.pse(heights)

        # now i have nse which is next smaller element and pse which is previous smaller element
        # so the concept is that is let's say that i am at ith candidat rectangle, i can strech till either next smaller rectangle or previous smaller recangle, next smaller and previous smaller is what limiting my width.
       
        max_area = float('-inf')
        area = 0

        for i in range(len(heights)):
           
            width = nse[i] - pse[i] - 1
           
            if width < 0:
                area = heights[i]
               
            else:
                area = heights[i]*width
            
            max_area = max(max_area, area)
            
        return max_area



    def nse(self, heights):
        nse = [len(heights)]*len(heights)
        stack = []

        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]]>heights[i]:
                stack.pop()

            if len(stack) == 0:
                pass
            else:
                nse[i] = stack[-1]
            stack.append(i)
        return nse

    def pse(self, heights):
        stack1 = []
        pse = [-1]*len(heights)

        for i in range(len(heights)):
            while stack1 and heights[stack1[-1]]>=heights[i]:
                stack1.pop()
            if len(stack1) == 0:
                pass
            else:
                pse[i] = stack1[-1]
            stack1.append(i)
        return pse