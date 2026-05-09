class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track_map = {}

        for i in range(len(nums)):
            track_map[nums[i]] = 1 + track_map.get(nums[i],0)
            if track_map[nums[i]] > 1:
                return True
        
        return False
        