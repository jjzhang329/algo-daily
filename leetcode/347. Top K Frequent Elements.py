#using a min-heap to save all items, once size > k
#popup from top

from collections import Counter
import heapq


def topKFrequent(nums, k):
    count = Counter(nums)
    top = []
    for key, freq in count.items():
        heapq.heappush(top, (freq,key))
        if len(top) > k:
            heapq.heappop(top)
    
    res = []
    while len(res) < k:
        res.append(heapq.heappop(top)[1])
    
    return res