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

        for i in range(len(nums)):

            min_index = i

            for j in range(i, len(nums)):
                if nums[j]<nums[min_index]:
                    min_index = j
            
            nums[i], nums[min_index] = nums[min_index], nums[i]
          
        