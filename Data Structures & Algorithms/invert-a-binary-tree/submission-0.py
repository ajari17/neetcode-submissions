# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.reverser(root)

    def reverser(self, node):
        if node is None:
            return node
        node.left, node.right = node.right, node.left
        self.reverser(node.right) 
        self.reverser(node.left)
        return node