class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # we are given an integer array of nums and let us consider that array of nums
        # is A = [1, 2, 3, 4]
        # result array where ans[i] == nums[i]
        # ans[i+n] = nums[i]
        # n is the lenght of that aray
        # basically ans is concatanation of two nums arrays


        return nums + nums

        