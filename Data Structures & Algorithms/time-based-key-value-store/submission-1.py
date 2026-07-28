class TimeMap:

    def __init__(self):
        self.hash_table = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_table:
            self.hash_table[key] = []
    
        self.hash_table[key].append([value,timestamp])    

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_table:
            return ""
        
        arr = self.hash_table.get(key)
        res = ""
        l, r = 0, len(arr) - 1

        while l <= r:
            m = l + (r - l)//2

            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
        

        
