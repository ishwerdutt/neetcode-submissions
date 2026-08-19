class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # linear search; easy appraoch
        # time complexity = O(N)


        peak = float('-inf')
        peak_ind = None


        # for i in range(len(nums)):
        #     if nums[i]>peak:
        #         peak = nums[i]
        #         peak_ind = i
        # return peak_ind


        # it is working and beating 99.60% submissions.
        # the question is that how i ca do in O(log(n)) time. 
        # must be related to reduced searcg space.
        # but let's see on ipad, how can we do it??????

        l = 0
        r = len(nums) - 1

        

        while l<r:
            mid = l + (r-l)//2


            if nums[mid]>nums[mid+1]:
                r = mid    
            else:
                l = mid+1
                
                    

        return l


        # okay this piece of code returning the correct peak element, only work left to do is returning the index of 

        