# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        while head and head.next:
            head = head.next.next
            slow = slow.next 
            if head == slow:
                return True
        return False