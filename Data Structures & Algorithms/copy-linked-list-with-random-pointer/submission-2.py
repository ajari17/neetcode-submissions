"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None:None} # for an edge case its None:None
        
        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val)#in the map the key is the current node and the value is a new node initialized with the current nodes val
            cur = cur.next
        #map = {3:3,7:7,...} key is original node, val is new node same val
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
        
        