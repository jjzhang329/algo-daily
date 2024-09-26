# UnionFind class
# optimized find using recursion, and rank
# Time Complexity: O(a(N)) inverse ackermann of N, which is close to constant
# Space: O(N)
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
	# Some ranks may become obsolete so they are not updated
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Quick Union optimization by rank
# find, union, connected => O(log(n))

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Quick Union
# find => O(n)
# union => depends on find
# difference is for the root array, we save the parent node
# for quick find, we save the root node
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Quick Find
# find, connected => O(1)
# Union = > O(n)
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Test Case
uf = UnionFind(10)
print(uf.root)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
print(uf.root)
uf.union(2, 5)
print(uf.root)
uf.union(5, 6)
print(uf.root)
uf.union(6, 7)
print(uf.root)
uf.union(3, 8)
print(uf.root)
uf.union(8, 9)
print(uf.root)

# print(uf.connected(1, 5))  # true
# print(uf.connected(5, 7))  # true
# print(uf.connected(4, 9))  # false
# # 1-2-5-6-7 3-8-9-4
# uf.union(9, 4)
# print(uf.connected(4, 9))  # true