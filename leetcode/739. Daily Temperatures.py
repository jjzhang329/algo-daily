# using a monotonic stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dq = [(temperatures[0], 0)]
        ans = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            current_temp = temperatures[i]
            
            while dq and current_temp > dq[-1][0]:
                idx = dq.pop()[1]
                ans[idx] = i -idx
            
            dq.append((current_temp, i))

        return ans