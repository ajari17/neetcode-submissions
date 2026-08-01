# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            checker = group_prev

            for _ in range(k):
                checker = checker.next
                if not checker:
                    return dummy.next

            group_next = checker.next

            prev = group_next
            cur = group_prev.next
            tail = cur

            for _ in range(k):
                save = cur.next
                cur.next = prev
                prev = cur
                cur = save

            group_prev.next = prev
            group_prev = tail



            

