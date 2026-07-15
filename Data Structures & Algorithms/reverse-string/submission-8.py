class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # in python it is kind of easy
        # even though this approach here is best approach, let's walk throught the stack approach

        # i = 0
        # j = len(s)-1

        # while i<j:
        #     if len(s)==0 or len(s)==1:
        #         break
        #     if s == s[::-1]:
        #         break
        #     s[i], s[j] = s[j], s[i]

        #     i = i+1
        #     j = j-1

        # but let us try the stack one

        # stack = []
        # for i in s:
        #     stack.append(i)

        # for i in range(len(stack)):
        #     s[i] = stack.pop()


        # let us implement the recursion thing

        # def reverse(l, r):
        #     if l<r:
        #         reverse(l+1, r-1)
        #         s[l], s[r] = s[r], s[l]

        # reverse(0, len(s)-1)     

        s.reverse()  