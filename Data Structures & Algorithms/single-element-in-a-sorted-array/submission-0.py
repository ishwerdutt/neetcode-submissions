class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # linear seasrch- easy

        count_set = dict()


        for i in range(len(nums)):
            count_set[nums[i]] = count_set.get(nums[i], 0)+1
        print(count_set)

        for i in nums:
            if count_set[i] == 1:
                return i
        return -1


        