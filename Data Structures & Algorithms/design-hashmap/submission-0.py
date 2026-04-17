class ListNode:
    def __init__(self, key:int, value: int):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.bucket = [ListNode(0,0) for _ in range(10**4)]
    
    def put(self, key: int, value: int) -> None:
        index = key % len(self.bucket)
        prev = self.bucket[index]
        curr = prev.next

        while curr is not None:
            if curr.key == key:
                curr.value = value
                return
            prev = curr
            curr = prev.next
        
        prev.next = ListNode(key,value)
        

    def get(self, key: int) -> int:
        index = key % len(self.bucket)
        prev = self.bucket[index]
        curr = prev.next

        while curr is not None:
            if curr.key == key:
                return curr.value
            prev = curr
            curr = prev.next
        
        return -1

    def remove(self, key: int) -> None:
        index = key % len(self.bucket)
        prev = self.bucket[index]
        curr = prev.next

        while curr is not None:
            if curr.key == key:
                curr.key = None
                return
            prev = curr
            curr = prev.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)