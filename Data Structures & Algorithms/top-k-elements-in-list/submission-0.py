class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}

        for num in nums:
            num_map[num] = num_map.get(num,0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in num_map.items():
            buckets[freq].append(num)
        
        result = []

        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    break
            if len(result) == k:
                break

        return result
        


            



            


            
            

        

        