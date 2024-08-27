class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        else:
            values = self.store[key]
            left, right = 0, len(values)-1
            if timestamp >= values[-1][1]:
                return values[right][0]

            while left <= right:
                mid = (left + right) // 2
                prev_time = values[mid][1]

                if timestamp == prev_time:
                    return values[mid][0]
                elif timestamp > prev_time:
                    left = mid+1
                else:
                    right = mid-1
            return ''



# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("love","high",10)
obj.set("love","low",20)
print(obj.get("love",5))
print(obj.get("love",10))
print(obj.get("love",15))
print(obj.get("love",20))
print(obj.get("love",25))