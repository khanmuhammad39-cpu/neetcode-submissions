# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        # None -> 1 -> 2 -> 3 -> 4 -> 5 -> None
        # None -> 1 -> 2 -> 3 -> None (first half)
        # None -> 4 -> 5 -> None (second half)
        # None -> 5 -> 4 -> None (reveresed second half)
        # None -> 1 -> 5 -> 2 -> 4 -> 3 -> None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        slow.next = None
        prev = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        start = head

        while prev:
            tmp_1 = prev.next
            tmp_2 = start.next

            start.next = prev
            prev.next = tmp_2

            start = tmp_2
            prev = tmp_1



        