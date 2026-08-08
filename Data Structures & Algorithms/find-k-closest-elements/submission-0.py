class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        diff_arr = [0] * len(arr)

        for i in range(len(arr)):
            diff_arr[i] = abs(arr[i]-x)
        print(diff_arr)

        indices = sorted(range(len(diff_arr)), key=lambda i: diff_arr[i])[:k]
        print(indices)

        ans = []

        for i in indices:
            ans.append(arr[i])
        ans.sort()
        return ans
   