class ListNode:
    def __init__(self,key, val, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.hashmap = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.remove(node)
        self.add_at_tail(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove(node)
            self.add_at_tail(node)
        else:
            node = ListNode(key,value)
            self.hashmap[key] = node
            self.add_at_tail(node)

            if len(self.hashmap) > self.size:
                lru = self.head.next
                self.remove(lru)
                del self.hashmap[lru.key]

    
    def remove(self, node):
        node.prev.next = node.next # A -> C 
        node.next.prev = node.prev
    
    def add_at_tail(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.next = self.tail
        node.prev = prev_node
        self.tail.prev = node
        
