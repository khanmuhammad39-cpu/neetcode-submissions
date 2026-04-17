class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        result = []

        for idx, num in enumerate(nums):
            need = target - num
            if need in num_map:
                return [num_map[need], idx]
            num_map[num] = idx
        
        return []
