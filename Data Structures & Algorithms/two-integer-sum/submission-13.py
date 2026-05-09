class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {} # val -> index

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev_nums:
                return [prev_nums[diff], i]
            prev_nums[nums[i]] = i

        return []        