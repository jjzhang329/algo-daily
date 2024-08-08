class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right

# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
root = Node(3)
node_a = Node(9)
node_b = Node(20)
node_c = Node(15)
node_d = Node(7)
root.left = node_a 
root.right = node_b 
node_b.left = node_c
node_b.right = node_d

# using BFS to traverse all nodes, and record columns
# using defaultdict to have column: [nodes] pairs
# and from min_colmn to max_column, loop thru and build result

from collections import deque, defaultdict

def verticalOrder(root):
    if root == None:
        return []

    table = defaultdict(list)
    min_column, max_column = 0, 0 
    queue = deque([(root, 0)])
    while queue:
        node, column = queue.popleft()
        if node:
            table[column].append(node.val)
            min_column = min(min_column, column)
            max_column = max(max_column, column)
            queue.append((node.left, column-1))
            queue.append((node.right, column+1))
    
    result = []
    for i in range(min_column, max_column+1):
        result.append(table[i])
    
    return result

print(verticalOrder(root))