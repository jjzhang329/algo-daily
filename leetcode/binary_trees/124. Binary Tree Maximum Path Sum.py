# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -float("inf")

        def dfs(root):
            nonlocal result
            if root == None:
                return 0

            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            result = max(result, left + right + root.val)
            return max(left, right) + root.val

        dfs(root)
        return result