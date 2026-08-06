class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)

        if n1>n2:
            return False

        count_s1 = {}
        count_s2 = {}

        for i in range(len(s1)):
            count_s1[s1[i]] = count_s1.get(s1[i], 0)+1

        print(count_s1)

        l = 0
        r = 0


        while r<n2:
            count_s2[s2[r]] = count_s2.get(s2[r], 0)+1

            
            while r-l+1>n1:
                print(count_s2[s2[l]])
                count_s2[s2[l]]-=1
                if count_s2[s2[l]] == 0:
                    del count_s2[s2[l]]
                l = l+1
            if count_s1 == count_s2:
                return True
            r = r+1
        return False
            

        