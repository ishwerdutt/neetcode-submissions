class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]

        # let us try the binary search solution
        for i in range(len(numbers)):

            left, right = i, len(numbers)-1
            temp = target - numbers[i]
            
            while left<=right:
                mid = (left+right)//2
                if temp == numbers[mid]:
                    return [i+1, mid+1]
                elif temp>numbers[mid]:
                    left = mid + 1
                else:
                    right = mid-1
        return []
        