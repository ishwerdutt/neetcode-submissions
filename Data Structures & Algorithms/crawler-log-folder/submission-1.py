class Solution:
    def minOperations(self, logs: List[str]) -> int:

        # this is a file system that keeps a log each time some user performs a change folder operation


        depth = 0

        for log in logs:
            if log == "../":
                if depth > 0:
                    depth-=1
            elif log == "./":
                #here i will do nothing
                continue
            else:
                depth+=1
        return depth
        
        