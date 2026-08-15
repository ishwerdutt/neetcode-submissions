class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # i have n cars travelling to the same destination on one lane highway
        # position and speed

        # reach_set = set()

        # for i in range(len(position)):
        #     reach_set.add((target-position[i])//speed[i])

        # return len(reach_set)

        # this was brute force but it never worked, like my love life never worked, but it is what it is....


        # hm kya krenge, apun krenge sorting, hm cars ko sort krenge, jo cars target ke sbse jyada nazdeek hain


        cars = sorted(zip(position, speed), reverse = True)
        
        
        # now if car behind has arrival_time greater than the car ahead, then it is a new fleet     
        stack = []
        for pos, speed in cars:
            time_to_arrival  = (target-pos)/speed
            if not stack or time_to_arrival>stack[-1]:
                stack.append(time_to_arrival)
        
        return len(stack)
        