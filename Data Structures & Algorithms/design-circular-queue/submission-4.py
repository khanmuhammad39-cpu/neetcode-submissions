class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.nodes = [ListNode(None,None) for i in range(self.size)]
        for i in range(self.size):
            self.nodes[i].next = self.nodes[(i + 1) % self.size]
        
        self.head = self.nodes[0]
        self.tail = self.nodes[0]
        self.count = 0

        
    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.tail.val = value
        self.tail = self.tail.next
        self.count += 1
        return True



    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = self.head.next
        self.count -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.head.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        tmp_tail = self.head
        
        for i in range(self.count - 1):
            tmp_tail = tmp_tail.next
        
        return tmp_tail.val

        

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False
        
        

    def isFull(self) -> bool:
        if self.count == self.size:
            return True
        else:
            return False
        


        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()