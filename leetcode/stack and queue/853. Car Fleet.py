# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

# Output: 3
# Explanation:
# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. 
# The fleet forms at target.
# The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. 
# The fleet moves at speed 1 until it reaches target.

#后面的追赶前面的，用stack记录每辆车需要多久到达目的地点
#如果当前需要时间小于前一个，说明可以和前一辆车fleet,然后把当前车去掉，因为fleet后根据前车速度前进
# 最后stack剩下多少车就是多少个fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos  = []
        for i in range(len(position)):
            pos.append((position[i], speed[i]))
        stack = []

        pos.sort(reverse=True)

        for p, s in pos:
            time_needed = (target-p) / s
            stack.append(time_needed)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
            
        return len(stack)