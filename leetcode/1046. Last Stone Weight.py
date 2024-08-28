# we need to use max_heap, and we can change all nums to nums*-1
# then we can use the built in heapq which is a min_heap
from collections import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1*stones[i]
        
        heapq.heapify(stones)
        
        #[-8,-7,-4,-2,-1,-1]
        while len(stones) > 1:
            first = heapq.heappop(stones) # -8
            second = heapq.heappop(stones) # -7
            if first != second:
                heapq.heappush(stones, first-second)
        
        return 0 if not stones else -heapq.heappop(stones)