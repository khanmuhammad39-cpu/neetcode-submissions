class ListNode:
    def __init__(self, key:int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.bucket = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.bucket)
        prev = self.bucket[index]
        curr = prev.next

        while curr is not None:
            if curr.key == key:
                return
            prev = curr
            curr = prev.next
        
        prev.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        index = key % len(self.bucket)
        prev = self.bucket[index]
        curr = prev.next

        while curr is not None:
            if curr.key == key:
                curr.key = None
            prev = curr
            curr = prev.next
        

    def contains(self, key: int) -> bool:
        index = key % len(self.bucket)
        prev = self.bucket[index]
        curr = prev.next

        while curr is not None:
            if curr.key == key:
                return True
            prev = curr
            curr = prev.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)