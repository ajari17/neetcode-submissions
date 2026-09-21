# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        nodes = deque([root])
        res = []
        while nodes:
            node_amt = len(nodes)
            cur_nodes = []
            for _ in range(node_amt):
                cur = nodes.popleft()
                cur_nodes.append(cur.val)
                if cur.left: nodes.append(cur.left)
                if cur.right: nodes.append(cur.right)
            res.append(cur_nodes)
        return res

            

        