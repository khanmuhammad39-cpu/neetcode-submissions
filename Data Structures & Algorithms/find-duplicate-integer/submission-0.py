class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        bool_val = True

        while bool_val:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                bool_val = False
            else:
                continue
        
        start = 0
        bool_val = True

        while bool_val:
            start = nums[start]
            slow = nums[slow]
            if start == slow:
                return slow
            else:
                continue

        
        
        

        
        