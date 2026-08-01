# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,root.val)
    def dfs(self,node,maxx):
        is_good = 0
        if node == None:
            return 0
        if node.val >= maxx: 
            is_good = is_good + 1
        maxx = max(node.val, maxx)
        return self.dfs(node.left,maxx) + self.dfs(node.right,maxx) + is_good

            

    