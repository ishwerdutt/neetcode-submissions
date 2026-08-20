class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        # brute force:
        # two loops:

        # pairs_diff = set()

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         pairs_diff.add(abs(nums[i] - nums[j]))
        # print(pairs_diff)

        # pairs_diff = list(pairs_diff)
        # return max(pairs_diff[:p])

        nums.sort()
        def can_make_pairs(x):
            pairs = 0
            i = 0

            while i<=len(nums)-2:
                if nums[i+1]-nums[i]<=x:
                    pairs+=1
                    i = i+2
                else:
                    i = i+1
            return pairs>=p

        l = 0
        r = nums[-1]-nums[0]

        while l<r:
            mid = l + (r-l)//2

            if can_make_pairs(mid):
                r = mid
            else:
                l = mid+1
        return l
               