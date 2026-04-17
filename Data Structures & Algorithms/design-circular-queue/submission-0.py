class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.array = [0 for i in range(k)] 
        self.head = 0
        self.tail = 0
        self.count = 0
        
    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.array[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.count += 1
        return True



    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.array[self.head]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.array[self.tail - 1]
        

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.count > self.size - 1:
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