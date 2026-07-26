class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #let us do this two pointer approach
        right = len(nums)-1
        k = k%(len(nums))

        while k:
            temp = nums[right]
            j = len(nums) - 1
            
            while j>0:
                nums[j] = nums[j-1]
                j = j-1
            nums[j] = temp
            k = k-1
        print(nums)
            
            
       
        