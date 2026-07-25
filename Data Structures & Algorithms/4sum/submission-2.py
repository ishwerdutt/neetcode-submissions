class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = [] # cause there can be multiple answers
        nums.sort()

        # 

        for i in range(len(nums)):
            
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
            # we are just skiiping the repeating value at nums[i]
                l = j+1
                r = len(nums)-1
                while l<r:
                    curr = nums[i] + nums[j] + nums[l] + nums[r]
                    if curr == target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l+=1
                        r-=1

                        while l<r and nums[l] == nums[l-1]:
                            l+=1
                        while l<r and nums[r] == nums[r+1]:
                            r-=1
                    elif curr>target:
                        r = r-1
                    else:
                        l = l+1
        return ans
            