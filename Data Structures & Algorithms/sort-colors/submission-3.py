class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0 #this will traverse the whole array
        j = len(nums) - 1 # this will track values 2
        k = 0 # this will track values 0

        while i <= j:
            if nums[i] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                
            else:
                i += 1
        