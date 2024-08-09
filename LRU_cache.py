# using python3's built-in orderedDict
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.cache = OrderedDict()
    
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1
    
    def put(self, key, value):            
        self.cache[key] = value
        self.cache.move_to_end(key)

        if self.capacity < len(self.cache):
            self.cache.popitem(False)
        
#using double linked list
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        

class Cache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail 
        self.tail.prev = self.head
    
    def add(self, node):
        #adding node to the end, and next = dummy tail
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        previous_next = node.next 
        prev = node.prev
        prev.next = previous_next
        previous_next.prev = prev
    
    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            old_node = self.dic[key]
            self.remove(old_node)

        node = ListNode(key, value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

obj = LRUCache(2)
obj.put(1,1)
print(obj.cache)
obj.put(2,2)
print(obj.cache)
print(obj.get(1)) # => 1
obj.put(3,3)
print(obj.cache)
obj.get(2) # => -1
obj.put(4,4)
print(obj.cache)
obj.get(1)
print(obj.cache)
obj.get(3)
print(obj.cache)
obj.get(4)
print(obj.cache)
    