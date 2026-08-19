class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        def days_needed(weights, mid):
            days = 1 # first day
            curr_wt = 0

            for wt in weights:
                if curr_wt+wt > mid:
                    days+=1
                    curr_wt = wt
                else:
                    curr_wt+=wt
            return days
        
        l = 1
        r = sum(weights)
        print(sum(weights))

        while l<r:
            mid = l + (r-l)//2
            print("mid", mid)
            days_need = days_needed(weights, mid)
            print("days_needed", days_need)

            if days_need<=days:
                r = mid
            else:  # days_needed>days: # 1, 3, 4, 5, 6
                l = mid+1
            print(r, l)
        return max(l, max(weights))

        
        