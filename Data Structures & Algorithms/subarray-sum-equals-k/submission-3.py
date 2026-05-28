class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {}
        prefix_map[0] = 1
        prefix_sum = 0
        counter = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            need = prefix_sum - k
            counter += prefix_map.get(need,0)
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum,0) + 1
        
        return counter