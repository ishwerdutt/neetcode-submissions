class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hash_map  = dict(Counter(nums))

        print(hash_map)
        max_key = max(hash_map, key=hash_map.get)

        return max_key 

        

        