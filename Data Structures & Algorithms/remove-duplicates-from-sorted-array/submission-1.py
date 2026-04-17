class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = i + 1
        k = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                k += 1
                nums[i+1] = nums[j]
                i += 1
                j += 1
        
        return k
        