class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:


        # num_arrs = 0
        # l = 0
        # for r in range(k-1, len(arr)):
        #     avg = 0
        #     sum_of_arr = 0
        #     for i in range(l, r+1):
        #         sum_of_arr = sum_of_arr+arr[i]

        #     avg = sum_of_arr/k
        #     if avg>=threshold:
        #         num_arrs = num_arrs+1
        #     l = l+1
        # return num_arrs


        # okay i have got the optimal appraoch in my mind

        sum_of_arr = 0
        nums_arr = 0
        for i in range(k):
            sum_of_arr = sum_of_arr+arr[i]
        if sum_of_arr/k >= threshold:
            nums_arr+=1
        

        l = 0
        for r in range(k, len(arr)):
            sum_of_arr = sum_of_arr-arr[l]
            sum_of_arr = sum_of_arr+arr[r]
            l = l+1
            if sum_of_arr/k >= threshold:
                nums_arr+=1
        return nums_arr
            