# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start,dummy = head,head
        lenn = 0
        while head:
            lenn += 1
            head = head.next
        if lenn - n == 0:
            return start.next
        for i in range(lenn - n-1):
            start = start.next
        start.next = start.next.next
        return dummy
