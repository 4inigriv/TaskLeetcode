# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,summ):
            if node is None:
                return False
            summ += node.val
            if node.left is None and node.right is None:
                if summ == targetSum:
                    return True
            return dfs(node.left, summ) or dfs(node.right, summ)
        return dfs(root, 0)


        