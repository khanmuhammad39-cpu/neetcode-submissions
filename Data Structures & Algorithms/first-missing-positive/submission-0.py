class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique_set = set(nums)

        for i in range(1,len(nums)+2,1):
            if i in unique_set:
                continue
            else:
                return i
        