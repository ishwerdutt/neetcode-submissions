class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 0
        def time_needed(k):
            total_hrs = 0

            for pile in piles:
                total_hrs += (pile + k - 1) // k

                if total_hrs > h:
                    return total_hrs

            return total_hrs

        while l<=r:
            mid = l + (r-l)//2

            total_hrs = time_needed(mid)

            if total_hrs<=h:
                ans = mid
                r = mid - 1
            else:
                l = mid+1
        return ans


        