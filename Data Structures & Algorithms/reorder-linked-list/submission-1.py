# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        

        
        prev2 = None
        cur = slow.next
        slow.next = None

        while cur:
            tmp = cur.next
            cur.next = prev2
            prev2 = cur
            cur = tmp
        
        start = head

        while prev2:
            tmp_1 = prev2.next
            tmp_2 = start.next

            start.next = prev2
            prev2.next = tmp_2

            start = tmp_2
            prev2 = tmp_1
        
        return
        


        
