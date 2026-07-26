class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #let us do this two pointer approach
        # right = len(nums)-1
        # k = k%(len(nums))

        # while k:
        #     temp = nums[right]
        #     j = len(nums) - 1
            
        #     while j>0:
        #         nums[j] = nums[j-1]
        #         j = j-1
        #     nums[j] = temp
        #     k = k-1
        # print(nums)
        
        # time limit is getting exceeded in leetcode
        # another approach but with some space complexity



        temp_arr = [0]*len(nums)
        n = len(nums)
        k = k%n

        for i in range(n):
            temp_arr[(i+k)%n] = nums[i]
        

        print(temp_arr)


        for i in range(len(nums)):
            nums[i] = temp_arr[i]

        print(nums)
            
       
        