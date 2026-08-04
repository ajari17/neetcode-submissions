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
        oldToCopy = {None:None}#for edge case set it as this
        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val)#in the hashmap map the current node to a new node with its value
            cur = cur.next
        cur = head#reset cur
        while cur:
            copy = oldToCopy[cur]#retrive the new node with the key being the current node
            copy.next = oldToCopy[cur.next]#set new nodes next to the value of the next node using map
            copy.random = oldToCopy[cur.random]#same thing as next but we use .random
            cur = cur.next
        return oldToCopy[head]#return the new linkedlist 
            
