# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(None)
        dummy.next = head

        start = dummy
        prev = dummy

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
        #
        # Example:
        # original list: 1 -> 2 -> 3 -> 4 -> 5
        # left = 2, right = 4
        #
        # after this loop:
        # prev  = 1
        # start = 2
        #
        # so the list is still:
        # dummy -> 1 -> 2 -> 3 -> 4 -> 5
        #          prev   start

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
        # prev      -> node before reversed section
        # left_node -> original left-th node, now tail of reversed section
        # prev_2    -> new head of reversed section
        # cur       -> first node after reversed section
        #
        # Example:
        # original list: 1 -> 2 -> 3 -> 4 -> 5
        # left = 2, right = 4
        #
        # reversal steps:
        # 2 -> None
        # 3 -> 2 -> None
        # 4 -> 3 -> 2 -> None
        #
        # pointers now are:
        # prev      = 1
        # left_node = 2
        # prev_2    = 4
        # cur       = 5
        #
        # so the pieces look like:
        # 1 -> 2 -> None
        # 4 -> 3 -> 2 -> None
        # cur -> 5
        #
        # after reconnecting:
        # prev.next = prev_2      makes 1 -> 4
        # left_node.next = cur    makes 2 -> 5
        #
        # final list:
        # 1 -> 4 -> 3 -> 2 -> 5

        prev.next = prev_2
        left_node.next = cur

        return dummy.next