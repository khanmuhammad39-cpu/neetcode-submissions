# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Null -> 1 -> 2 -> 3 -> Null
        # Null -> 1 -> 2 -> 3 -> 4 -> Null

        slow = head
        fast = head.next

        #odd
        # prev will be at 1 (end of the first half)
        # fast will be at Null (end of second half)
        # slow will be at 2 (start of the second half)

        #even
        # prev will be at 1 (end of the first half)
        # fast will be at 4 (end of second half)
        # slow will be at 2 (start of the second half)

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        #reversing the second half
        
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # -> 4 -> 5 -> 6 -> None to 6 -> 5 -> 4 -> Null
        # prev is at 6
        # 1 -> 2 -> 3 -> None
        # 6 -> 5 -> 4 -> None

        first = head

        while prev:
            tmp_1 = prev.next
            tmp_2 = first.next

            first.next = prev
            prev.next = tmp_2

            first = tmp_2
            prev = tmp_1

        
        return prev







