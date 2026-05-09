from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        #first window
        for r in range(0,k):
            cur_num = nums[r]
            while dq and cur_num >= nums[dq[-1]]:
                dq.pop()
            dq.append(r)
        
        res.append(nums[dq[0]])
        
        # rest of the windows
        for i in range(k,len(nums)):
            cur_num = nums[i]
            if dq[0] < i - k + 1:
                dq.popleft()
            while dq and cur_num >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            res.append(nums[dq[0]])
        
        return res



        