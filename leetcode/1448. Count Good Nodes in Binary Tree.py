# counting the nodes that satisfy a condition
# use a matcher, and go thru all nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float('-inf'))

    def dfs(self, root, max_value):
        if root == None:
            return 0 
        count = 0

        if root.val >= max_value:
            count = 1
        
        max_value = max(max_value, root.val)
        left = self.dfs(root.left, max_value)
        right = self.dfs(root.right, max_value)

        return count + left + right 