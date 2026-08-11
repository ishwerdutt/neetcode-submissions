class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # at the beginning of the game, i start with empty record

        # given a list of strings operations, where operations[i] is the ith operation i must apply to the record and is one of the following
        # int x:- record new score x
        # + = record new score that is some of prev two
        # D =  record new score that is dpuble of prev
        # C = invalid prev score, remove it from the score
        # ofcourse i ruined everything, it was supposed be a friendship, butttt faaahhhh why the fuck i fall for her, and now guess what she has abandoned me

        scores_stack = []
        score = 0
        top = -1

        for op in operations:
            if op == "+":
                scores_stack.append(scores_stack[len(scores_stack)-1]+scores_stack[len(scores_stack)-2])
                
            elif op == "D":
              
                scores_stack.append(scores_stack[len(scores_stack)-1]*2)
            
            elif op == "C":
                scores_stack.pop()
              
            else:
            
                scores_stack.append(int(op))
                print(scores_stack)

        return sum(scores_stack)

                    




        