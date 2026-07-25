class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = [] # cause there can be multiple answers
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                current = nums[i] + nums[l] + nums[r] 
                if current == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                        
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                        
                elif current>0:
                    r = r-1
                else:
                    l = l+1   
        return ans
