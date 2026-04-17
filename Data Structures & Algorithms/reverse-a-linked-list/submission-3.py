# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur is not None:
            tmp = cur.next #save next
            cur.next = prev # reverse it
            prev = cur # move prev ahead
            cur = tmp #traverse
        
        return prev


        