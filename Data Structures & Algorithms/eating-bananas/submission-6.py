class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 0
        def time_needed(piles, mid):
            total_hrs = 0

            for i in range(len(piles)):
                total_hrs += (piles[i]+mid-1)//mid  

            return total_hrs

        while l<=r:
            mid = l + (r-l)//2

            total_hrs = time_needed(piles, mid)

            if total_hrs<=h:
                ans = mid
                r = mid - 1
            else:
                l = mid+1
        return ans


        