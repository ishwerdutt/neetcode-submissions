class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        # l = 0
        # r = k-1
        # min_white = float('inf')

        # for r in range(k-1, len(blocks)):
        #     num_whites = 0
        #     for l in range(r-k+1,r+1):
        #         if blocks[l] == "W":
        #             num_whites+=1
        #             print(num_whites)
        #     min_white = min(min_white, num_whites)

        # return min_white


        
        # first we will count the whites in first window:

        num_whites = 0
        for i in range(k):
            if blocks[i] == "W":
                num_whites = num_whites+1  # here we have counted the whites in first window
            
        l = 0
        min_whites = num_whites
        for r in range(k, len(blocks)):
            #k = 8
            # window size has been increased
            if blocks[l] == "W":
                num_whites = num_whites-1
            
            l = l+1

            # but agr r index pr hmein white mila, to apne ko white increse bhi krna pdega

            if blocks[r] == "W":
                num_whites = num_whites+1

            min_whites = min(min_whites, num_whites)
        return min_whites

