class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # [2,1,5,1,5,3]
        # sliding window will vary until >= target
        # keep track of window when window >= target
        prefix_sum = 0
        left = 0
        best_window = 2*len(nums) 
        for i in range(len(nums)):
            prefix_sum += nums[i]
            while prefix_sum >= target:
                window_size = i - left + 1
                best_window = min(window_size,best_window)
                prefix_sum -= nums[left]
                left += 1
            
        return best_window if best_window < 2*len(nums) else 0
            



        