# Input: root = [1,2,3,null,4], distance = 3
# Output: 1
# Input: root = [1,2,3,4,5,6,7], distance = 3
# Output: 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#brute force解法 O(n^3), 把每个节点数据返回，
from collections import defaultdict
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs = 0

        def dfs(root):
            if root == None:
                return defaultdict(int)

            if not root.left and not root.right:
                count = defaultdict(int)
                count[1] = 1
                return count

            left_dis = dfs(root.left)
            right_dis = dfs(root.right)

            for dl in left_dis:
                for dr in right_dis:
                    if dl + dr <= distance:
                        self.pairs += left_dis[dl] * right_dis[dr]

            all_dist = defaultdict(int)
            for d in left_dis:
                if d + 1 <= distance:
                    all_dist[d + 1] += left_dis[d]

            for d in right_dis:
                if d + 1 <= distance:
                    all_dist[d + 1] += right_dis[d]

            return all_dist

        dfs(root)
        return self.pairs