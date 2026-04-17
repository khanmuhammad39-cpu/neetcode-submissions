class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num,0) + 1
            if num_map[num] > 1:
                return True
        
        return False