class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """

        # array of nums = [] consisting of n elements
        #0=> represents red
        #1=>represents white



        # in place sorting algorithms hoti hai apne pass bubble sort, insertion sort and selection sort
        # Bubble sort solution for this

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]>nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]

        #selection sort

        # for i in range(len(nums)):

        #     min_index = i

        #     for j in range(i, len(nums)):
        #         if nums[j]<nums[min_index]:
        #             min_index = j
            
        #     nums[i], nums[min_index] = nums[min_index], nums[i]

        

        # we can apply counting sort here cause only limited number of 0, 1 and 2's are here
        # and then ofcourse we can overwrite the array

        nos_0 = 0
        nos_1 = 0
        nos_2 = 0

        for i in nums:
            if i == 0:
                nos_0 += 1
                
            elif i == 1:
                nos_1 = nos_1+1
                
            else:
                nos_2 +=1
        print(nos_0, nos_1, nos_2)

        # for i in range(nos_0):
        #     nums[i] = 0
            
        # for j in range(nos_0, nos_0+nos_1):
        #     nums[j] = 1
           
        # for k in range(nos_0+nos_1, len(nums)):
        #     nums[k] = 2

        
        nums[0:nos_0] = [0]*nos_0
        nums[nos_0:nos_0+nos_1] = [1]*nos_1
        nums[nos_0+nos_1:len(nums)] = [2]*nos_2

            


          
        