# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return 
        
        slow = head 
        fast = head
        print("got here")
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        split_end = slow.next
        slow.next = None
        prev = None
        while split_end:
            temp = split_end.next
            split_end.next = prev
            prev = split_end
            split_end = temp
        print("got here")
        # 2->4 and 8->6->None
        first, second = head, prev#prev = 8 (head of the second)
        while second:
            temp_first = first.next
            temp_second = second.next
            first.next = second
            second.next = temp_first
            first = temp_first
            second = temp_second
        head = prev
            
            
            