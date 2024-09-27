# dijkstr algo is used to find minimum, shortest solution in a weighted graph
# key is to use a heap to keep the smallest value in the top
# and use an min array to keep track of the value
# so everytime we pop from the hp, we are looking at smallest neighbors

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        steps = [ float('inf') ] * n
        graph = {}

        for i in range(n):
            graph[i] = []

        for a, b, price in flights:
            graph[a].append((b, price))
        
        hq = [(0, 0, src)]
        while hq:
            price, stops, node = heapq.heappop(hq)

            if stops > steps[node] or stops > k + 1:
                continue
            steps[node] = stops
            if node == dst:
                return price

            for neighbor, cost in graph[node]:
                heapq.heappush(hq, (cost+price, stops+1, neighbor))
    
        return -1