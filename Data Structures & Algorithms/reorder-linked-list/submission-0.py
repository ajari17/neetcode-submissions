# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        start = head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next       # Moves 1 step
            fast = fast.next.next  # Moves 2 steps
        end = slow.next
        slow.next = None
        prev = None
        while end:
            temp = end.next
            end.next = prev
            prev = end
            end = temp
        #######################
        end = prev#6,8
        #start = 2,4,6,8
        while end:
            t_start = start.next
            t_end = end.next
            start.next = end
            end.next = t_start
            start = t_start
            end = t_end
        head = end
            
        
        

        


            

