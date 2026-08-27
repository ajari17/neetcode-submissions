# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return
        
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        cur = slow.next
        slow.next = None
        prev = None
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        #0,1,2
        #6,5,4,3
        first,second = head, prev
        while second:
            t1,t2 = first.next,second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2
            
        
        
        
        