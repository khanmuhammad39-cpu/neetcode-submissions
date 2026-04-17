# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        start = ListNode(None)
        start.next = head
        prev = start

        counter_left = 0
        counter_right = 0

        # Move start to the left-th node
        while counter_left < left:
            prev = start
            start = start.next
            counter_left += 1
            counter_right += 1

        # At this point:
        # prev  -> node before left
        # start -> left-th node
        left_node = start

        cur = start
        prev_2 = None

        # Reverse nodes from left to right
        while counter_right <= right:
            tmp_1 = cur.next
            cur.next = prev_2
            prev_2 = cur
            cur = tmp_1
            counter_right += 1

        # After reversal:
        # prev   -> node before reversed section
        # left_node -> original left-th node, now tail of reversed section
        # prev_2 -> new head of reversed section
        # cur    -> first node after reversed section

        prev.next = prev_2
        left_node.next = cur

        return head if left > 1 else prev_2