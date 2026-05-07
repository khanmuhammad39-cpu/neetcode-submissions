class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxis = []
        max_val = 0

        for i in range(len(nums) - k + 1):
            max_val = nums[i]
            for j in range(i, i + k):
                max_val = max(max_val,nums[j])
            maxis.append(max_val)
        
        return maxis
