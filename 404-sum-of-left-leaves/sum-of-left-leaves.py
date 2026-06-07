# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sumt = 0
        if not root:
            return 0 
        def dfs(node, veio_da_esquerda):
            nonlocal sumt 
            if not node: 
                return 
            e_folha = not node.left and not node.right
            if e_folha and veio_da_esquerda:
                sumt += node.val 
            dfs(node.left, True)  
            dfs(node.right, False) #
        dfs(root, False)
        return sumt