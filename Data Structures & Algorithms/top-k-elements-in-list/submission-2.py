class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        max_freq = 0
        for i in range(len(nums)):
            frequency_map[nums[i]] = frequency_map.get(nums[i],0) + 1
            max_freq = max(max_freq,frequency_map[nums[i]])
        
        buckets = [[]for i in range(max_freq + 1)]
        print(buckets)

        for key, value in frequency_map.items():
            buckets[value].append(key)
        
        n = 0
        res = []
        for i in range(len(buckets)-1,-1,-1):
            if buckets[i] != []:
                for nums in buckets[i]:
                    res.append(nums)
                    n += 1
                    if n == k:
                        return res
        
        return res
        
        