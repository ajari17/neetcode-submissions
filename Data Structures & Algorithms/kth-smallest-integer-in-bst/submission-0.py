# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = deque()
        cur = root
        while nodes or cur:
            while cur:
                nodes.append(cur)
                cur = cur.left

            cur = nodes.pop()
            k = k - 1
            if k == 0: return cur.val
            cur = cur.right

        

