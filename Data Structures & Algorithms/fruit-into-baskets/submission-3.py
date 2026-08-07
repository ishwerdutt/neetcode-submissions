class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        basket = {}
        l = 0
        r = 0

        print("len", len(fruits))
        max_fruits = 0

        

        print(basket)

        while r<len(fruits):
            print("r", r)
            basket[fruits[r]] = basket.get(fruits[r], 0)+1

            while len(basket)>2:
                basket[fruits[l]]-=1
                if basket[fruits[l]]==0:
                    del basket[fruits[l]]
                l = l+1
            max_fruits = max(max_fruits, r-l+1)
            r = r+1
            print(basket)
        return max_fruits
        