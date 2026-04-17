# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        start_l_p = head
        left_counter = 0
        right_counter = 0

        while left_counter < left - 1 :
            prev = start_l_p
            start_l_p = start_l_p.next
            left_counter += 1
            right_counter += 1
        
        print(start_l_p.val) #start where reversal occurs
        print(prev.val) #before the reversed section
        print(left_counter)
        print(right_counter)

        prev_2 = ListNode(None)
        tail = start_l_p
        prev_2.next = tail

        for i in range(right - left + 1):
            tmp_1 = tail.next
            tail.next = prev_2
            prev_2 = tail
            tail = tmp_1
        
        
        prev.next = prev_2
        start_l_p.next = tail

        return dummy.next



