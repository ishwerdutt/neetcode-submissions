class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       

        def first_ap(nums, target):
            l = 0
            r = len(nums) - 1
            if len(nums) == 0:
                return -1


            while l < r:
                mid = l + (r - l) // 2

                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1

            if nums[l] == target:
                return l

            return -1


        def last_ap(nums, target):
            l = 0
            r = len(nums) - 1
            if len(nums) == 0:
                return -1


            while l < r:
                mid = l + (r - l + 1) // 2

                if nums[mid] <= target:
                    l = mid
                else:
                    r = mid - 1

            if nums[l] == target:
                return l

            return -1


        first_app = first_ap(nums, target)
        last_app = last_ap(nums, target)

        return [first_app, last_app]