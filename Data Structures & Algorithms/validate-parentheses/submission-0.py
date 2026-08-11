class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        

        for i in range(len(s)):
            # append only opening brackets
            if s[i] in "{[(":
                stack.append(s[i])

            else:
                # consider that no opening brackets were there => stack is empty
                if not stack or len(stack) == 0:
                    return False
                
                # # now we have to pop the top element and compare it with the next ch[i]
                # i will be on the index to the where all the opening brackets have been,

                top = stack.pop() # it will pop top element from the stack
                print(s[i])
                if top != pairs[s[i]]:
                    return False

        return (len(stack)==0)