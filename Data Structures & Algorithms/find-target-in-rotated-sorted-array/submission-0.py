class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        # we can always do linear search

        for i, num in enumerate(nums):
            print(i, num)
            if num == target:
                print(num == target)
                return i
        return -1
        