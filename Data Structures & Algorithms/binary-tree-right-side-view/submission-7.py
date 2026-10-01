# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        nodes = deque([root])
        res = []
        while nodes:
            n = len(nodes)
            for i in range(n):
                cur = nodes.popleft()
                if cur:
                    if (i == n-1):
                        res.append(cur.val)
                if cur.left: nodes.append(cur.left)
                if cur.right: nodes.append(cur.right)
        return res
            
        