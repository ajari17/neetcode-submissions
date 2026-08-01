# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    dia = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.dia
    def dfs(self,node):
        if not node:
            return 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        self.dia = max(self.dia,l+r)
        return 1 + max(l,r)