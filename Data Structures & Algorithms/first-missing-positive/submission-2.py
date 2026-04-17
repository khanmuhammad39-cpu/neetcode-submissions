class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        check = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                check += 1
            else:
                continue
        
        if check == 0:
            return 1
        
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1
        
        
        for i in range(len(nums)):
            n = abs(nums[i])
            if nums[n-1] > 0:
                nums[n-1] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        
        return len(nums) + 1
        

        