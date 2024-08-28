# trick is to use array to save global changing variables
# only add left or right if they are not < 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        self.dfs(root, res)
        return res[0]
    
    def dfs(self, node, res):
        if node == None:
            return 0 
        
        left = max(self.dfs(node.left, res),0)
        right = max(self.dfs(node.right, res), 0)
        res[0]= max(res[0], node.val+left+right)
    
        return node.val + max(left, right)