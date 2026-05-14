class ListNode:
    def __init__(self,key,value,next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode(None,None) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.hashmap)
        prev = self.hashmap[index]
        cur = prev.next

        while cur is not None:
            if cur.key == key:
                cur.value = value
                return
            prev = cur
            cur = cur.next
        
        prev.next = ListNode(key,value)

    def get(self, key: int) -> int:
        index = key % len(self.hashmap)
        prev = self.hashmap[index]
        cur = prev.next

        while cur is not None:
            if cur.key == key:
                return cur.value
            prev = cur
            cur = cur.next
        
        return -1
        

    def remove(self, key: int) -> None:
        index = key % len(self.hashmap)
        prev = self.hashmap[index]
        cur = prev.next

        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)