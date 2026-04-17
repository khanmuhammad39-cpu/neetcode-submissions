class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        prefix = 1
        suffix = 1

        for i in range(1,len(nums),1):
            prefix *= nums[i-1]
            res.append(prefix)
        
        for i in range(len(nums)-2,-1,-1):
            suffix *= nums[i+1]
            res[i] = res[i]*suffix
        
        return res
            
        