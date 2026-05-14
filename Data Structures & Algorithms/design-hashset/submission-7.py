class ListNode:
    def __init__(self,key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hash_set = [ListNode(None) for i in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.hash_set)
        cur = self.hash_set[index] # at dummy node

        while cur.next is not None:
            if cur.next.key == key:
                return
            cur = cur.next
        
        cur.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        index = key % len(self.hash_set)
        cur = self.hash_set[index] # at dummy node

        while cur.next is not None:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        
        return
        

    def contains(self, key: int) -> bool:
        index = key % len(self.hash_set)
        cur = self.hash_set[index] # at dummy node

        while cur.next is not None:
            if cur.next.key == key:
                return True
            cur = cur.next
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)