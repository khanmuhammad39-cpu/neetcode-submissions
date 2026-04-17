class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        suffix = 1

        for i in range(0,len(nums),1):
            if i == 0:
                res.append(1)
                continue
            prefix *= nums[i-1]
            res.append(prefix)
        
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                continue
            suffix *= nums[i+1]
            res[i] = res[i]*suffix
        
        return res
            
        