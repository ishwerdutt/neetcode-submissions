class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        #okay we will do this in merge sort

        def merge_sort(arr):
           

            if len(arr)<=1:
                return arr
            q = len(arr)//2

            left = merge_sort(arr[:q])
            right = merge_sort(arr[q:])

            return merge(left, right)

        

        def merge(arr1, arr2):
            merged_arr = []
            i=0
            j=0
            
            while i<len(arr1) and j<len(arr2):
                if arr1[i] <= arr2[j]:
                    merged_arr.append(arr1[i])
                    i+=1
                else:
                    merged_arr.append(arr2[j])
                    j+=1

            merged_arr.extend(arr1[i:])
            merged_arr.extend(arr2[j:]) 
            

            return merged_arr
        return merge_sort(nums)
        