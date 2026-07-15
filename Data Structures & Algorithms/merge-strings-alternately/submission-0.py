class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # looks easy

        # two pointer, one on first array and the other pointer will point to the second array

        i = 0
        j = 0
        total_len = len(word1)+len(word2)

        final_string = ""
        while i<len(word1) and j< len(word2):
            final_string+=word1[i]
            final_string+=word2[j]
            i=i+1
            j=j+1
        
        while i<len(word1):
            final_string+=word1[i]
            i=i+1
        while j<len(word2):
            final_string+=word2[j]
            j=j+1
        print(final_string)

        return final_string




        