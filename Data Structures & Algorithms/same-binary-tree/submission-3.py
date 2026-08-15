# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traverse(p,q)
    def traverse(self,node_p,node_q):
        if not node_p and not node_q:
            return True
        if node_p and not node_q:
            return False
        if not node_p and node_q:
            return False
        if node_p and node_q:
            if node_p.val != node_q.val:
                return False
            return self.traverse(node_p.left,node_q.left) and self.traverse(node_p.right,node_q.right)
        return True

