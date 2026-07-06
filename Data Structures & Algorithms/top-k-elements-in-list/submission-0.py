class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        int_set = {}
        for num in nums:
            int_set.setdefault(num, 0)
            int_set[num] += 1
        int_set = dict(sorted(int_set.items(), key=lambda item: item[1], reverse = True))
        
        empty_list:List[int] = []
        for keys in int_set:
            empty_list.append(keys)
        return empty_list[:k]
        