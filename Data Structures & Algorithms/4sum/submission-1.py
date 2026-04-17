class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        

        for i in range(0,len(nums)-3):
            if i > 0 and nums[i-1] == nums [i]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if nums [j-1] == nums[j] and j > i + 1:
                    continue
                k = j + 1
                l = len(nums) - 1

                while k < l:
                    tar = nums[i] + nums[j] + nums[k] + nums [l]
                    if tar < target:
                        k += 1
                        continue
                    elif tar > target:
                        l -= 1
                        continue
                    else:
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        k += 1
                        l -= 1
                        while nums[k-1] == nums [k] and k < l:
                            k += 1
                        while nums[l+1] == nums [l] and k < l:
                            l -= 1

        return res
                
            