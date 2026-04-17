# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge_list(l1,l2):
    dummy = ListNode(None)
    tail = dummy
    while l1 and l2:
        if l1.val >= l2.val:
            tail.next = l2
            l2 = l2.next
        else:
            tail.next = l1
            l1 = l1.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
            
    return dummy.next

class Solution:  
      
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = None

        for lst in lists:
            merged = merge_list(merged,lst)
        
        return merged


        