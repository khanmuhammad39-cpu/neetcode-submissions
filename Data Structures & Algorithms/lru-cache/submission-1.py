class ListNode:
    def __init__(self,key,val,prev=None,next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #maps key to node

        self.left = ListNode(None,None) #LRU
        self.right = ListNode(None,None) #Most recent
        # connecting the two nodes
        self.left.next = self.right
        self.right.prev = self.left
    
    #remove node from list
    def remove(self,node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev
        
        
    #insert/add node on the right
    def add(self,node):
        last_node = self.right.prev
        last_node.next = node
        node.prev = last_node
        self.right.prev = node
        node.next = self.right

    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            self.cache[key].val = value
        else:
            node = ListNode(key,value)
            self.cache[key] = node
            self.add(node)
            if len(self.cache) > self.capacity:
                first_node = self.left.next
                self.remove(first_node)
                del self.cache[first_node.key]

        
