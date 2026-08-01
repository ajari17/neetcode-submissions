# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        nodes = deque([root])
        while nodes:
            lvl = len(nodes)
            items = []
            for _ in range(lvl):
                cur = nodes.popleft()
                if cur.left: nodes.append(cur.left)
                if cur.right: nodes.append(cur.right)
                items.append(cur.val)
            res.append(items)
        return res