class ListNode:
    def __init__(self,key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hashset = [ListNode(None) for _ in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.hashset)
        prev = self.hashset[index] # head
        cur = prev.next

        while cur is not None:
            if cur.key == key:
                return
            prev = cur
            cur = cur.next
        
        prev.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        index = key % len(self.hashset)
        prev = self.hashset[index] # head
        cur = prev.next

        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        index = key % len(self.hashset)
        prev = self.hashset[index] # head
        cur = prev.next

        while cur is not None:
            if cur.key == key:
                return True
            prev = cur
            cur = cur.next
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)