class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.bucket = [[] for _ in range(self.size)]
    
    def hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        index = self.hash(key)
        bucket = self.bucket[index]

        for value in bucket:
            if value == key:
                return
        
        self.bucket[index] = bucket + [key]

    def remove(self, key: int) -> None:
        index = self.hash(key)
        bucket = self.bucket[index]
        
        new_bucket = []
        for value in bucket:
            if value != key:
                new_bucket = new_bucket + [value]

        self.bucket[index] = new_bucket

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        bucket = self.bucket[index]

        for value in bucket:
            if value == key:
                return True
        
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)