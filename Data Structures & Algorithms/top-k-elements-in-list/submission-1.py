class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}

        for num in nums:
            num_freq[num] = num_freq.get(num,0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key,value in num_freq.items():
            buckets[value].append(key)
        
        res = []

        for i in range(len(buckets)-1,0,-1):
            for val in buckets[i]:
                res.append(val)
                if len(res) == k:
                    return res
        
        return res
        