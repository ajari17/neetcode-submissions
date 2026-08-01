# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # Step 1: Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Cut the wire and reverse the second half
        end = slow.next
        slow.next = None
        prev = None
        
        while end:
            temp = end.next
            end.next = prev
            prev = end
            end = temp
            
        # Step 3: Clean Zipper Merge using simultaneous assignment
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            
            first.next = second
            second.next = t1
            
            first = t1
            second = t2
        