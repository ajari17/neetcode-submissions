# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.dfs(root,p,q)
    def dfs(self, node, p, q):
        #print((p.val <= node.val <= q.val) or (q.val <= node.val <= p.val))
        if node.val < p.val and node.val < q.val:
            return self.dfs(node.right, p , q)
        if node.val > p.val and node.val > q.val:
            return self.dfs(node.left, p , q)
        if (p.val <= node.val <= q.val) or (q.val <= node.val <= p.val):
            return node
        


