class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []


        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            need = -1*nums[i]
            j = i + 1
            k = len(nums) - 1
        
            while j < k:
                sum_t = nums[j] + nums[k]
                if sum_t < need:
                    j += 1
                elif sum_t > need:
                    k -= 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        
        return res


        