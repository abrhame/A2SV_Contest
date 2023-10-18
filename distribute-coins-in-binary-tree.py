# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        count = 0

        def dfs(node):
            nonlocal count
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            total = left + right + node.val - 1
            count += abs(total)
            return total

        dfs(root)
        return count