class Solution:
    def arrangeCoins(self, n: int) -> int:

        # i have n coins and i want to build a staircase with these coins. K rows in staircase. where the i th row has exacly i number of coins. The last row of staircase may be incomplete
        # return the number of complete rows of the staircase you will builf


        num_row = 0
        row = 1

        while n>=row:
            n = n-row
            num_row+=1
            row+=1
        return num_row