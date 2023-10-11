# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def helper(node, target,arr):

            if not node:
                return
            if not node.left and not node.right:
                if target - node.val == 0:
                    arr.append(node.val)
                    ans.append(arr.copy())
                    return
                else:
                    return


            helper(node.left,target - node.val,arr + [node.val])
            helper(node.right,target - node.val, arr + [node.val])
        if root:
            helper(root,targetSum,[])
        # print(ans)
        return ans