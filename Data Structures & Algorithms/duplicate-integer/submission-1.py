class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_map = {}

        for num in nums:
            if num in num_map:
                return True
            num_map[num] = num_map.get(num,0) + 1
        
        return False
        