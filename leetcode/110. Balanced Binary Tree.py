# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1

    def getHeight(self, root):
        if root == None:
            return 0 
        
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        if left == -1 or right == -1:
            return -1

        if abs(left-right) > 1:
            return -1
        else:
            return max(left, right) + 1