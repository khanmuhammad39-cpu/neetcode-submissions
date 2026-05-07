class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        max_list = []

        while r < len(nums):
            max_val = nums[l]
            for i in range(l, l + k):
                max_val = max(max_val,nums[i])
            max_list.append(max_val)
            l += 1
            r += 1
        
        return max_list
            

        