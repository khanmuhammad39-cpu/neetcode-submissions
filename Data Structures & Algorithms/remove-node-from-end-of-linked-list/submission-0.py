# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0

        start = head

        while start:
            counter += 1
            start = start.next
        
        if counter == n:
            return head.next
        
        again = head
        counter = counter - n
        while again:
            counter -= 1
            if counter == 0:
                again.next = again.next.next
                return head
            else:
                again = again.next
        
        return []



        