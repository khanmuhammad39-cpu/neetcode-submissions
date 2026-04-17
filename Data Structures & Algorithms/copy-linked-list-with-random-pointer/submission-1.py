"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_hashmap = {}
        cur = head

        if head is None:
            return None

        while cur:
            copy = Node(cur.val,None,None)
            copy_hashmap[cur] = copy
            cur = cur.next
        
        cur = head
        
        while cur:
            new_node = copy_hashmap[cur]
            new_node.next = copy_hashmap[cur.next] if cur.next else None
            new_node.random = copy_hashmap[cur.random] if cur.random else None
            cur = cur.next
        
        return copy_hashmap[head]

        