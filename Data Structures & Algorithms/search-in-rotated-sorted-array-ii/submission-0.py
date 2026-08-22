class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0 
        r = len(nums) - 1

        while l<=r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return True
            elif nums[mid] == nums[l] and  nums[mid] == nums[r]:
                l = l+1
                r = r-1
                continue

            elif nums[l]<=nums[mid]: 
                if nums[l] <= target and target<=nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if target>=nums[mid] and target <= nums[r]:
                    #eliminate the left half
                    l = mid+1
                else:
                    r = mid-1
        return False



      

        