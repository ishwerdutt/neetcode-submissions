class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # top most k elements nikalne hain apun ko

        
        nums_dict = dict(Counter(nums))
        sorted_data = dict(sorted(nums_dict.items(), key=lambda item: item[1], reverse = True))
        
        print(sorted_data)
        result_list = [key for key in sorted_data]
        return result_list[:k]
        