# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes = deque([root])
        res = []
        while nodes:
            size = len(nodes)
            for i in range(size):
                cur = nodes.popleft()
                if cur:
                    if cur and (size - 1 == i):
                        res.append(cur.val)
                    if cur.left: nodes.append(cur.left)
                    if cur.right: nodes.append(cur.right)

        return res
