class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # okay best time to buy and sell a stock
        # let see what the fuck in this problem

        # we have an integer array prices 
        #prices[i] = prices of neetcoin on the ith day

        # prices = [10,1,5,6,7,1] 
        #brute force solution for this is we do check for every pair

        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[i]<prices[j]:
        #             max_profit = max(max_profit, prices[j]-prices[i])
        # return max_profit


    # ofcaurse above is not the best solution available, let us find the best solution available

        max_profit = float('-inf')
        min_price = float('inf')

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            max_profit = max(max_profit, prices[i]-min_price)
        return max_profit


        