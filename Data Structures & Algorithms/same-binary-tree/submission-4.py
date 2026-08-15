# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traverse(p,[]) == self.traverse(q,[])

    def traverse(self,node,arr):
        if node == None:
            arr.append("Null")
        else:
            arr.append(node.val)
            self.traverse(node.left,arr)
            self.traverse(node.right,arr)
        return arr
        
        

        