class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        l = 0
        r = k-1
        min_white = float('inf')

        for r in range(k-1, len(blocks)):
            num_whites = 0
            for l in range(r-k+1, r+1):
                if blocks[l] == "W":
                    num_whites+=1
                    print(num_whites)
            min_white = min(min_white, num_whites)

        return min_white


        