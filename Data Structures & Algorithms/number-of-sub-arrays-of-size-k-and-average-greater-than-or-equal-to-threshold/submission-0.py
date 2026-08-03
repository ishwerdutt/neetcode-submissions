class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:


        num_arrs = 0
        l = 0
        for r in range(k-1, len(arr)):
            avg = 0
            sum_of_arr = 0
            for i in range(l, r+1):
                sum_of_arr = sum_of_arr+arr[i]

            avg = sum_of_arr/k
            if avg>=threshold:
                num_arrs = num_arrs+1
            l = l+1
        return num_arrs
            