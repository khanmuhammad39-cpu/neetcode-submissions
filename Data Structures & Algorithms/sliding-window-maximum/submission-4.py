class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        res = []
        l = 0

        for r in range(len(nums)):
            cur_num = nums[r]
            while dq and cur_num > nums[dq[-1]]:
                dq.pop()
            
            dq.append(r)

            if dq[0] < l:
                dq.popleft()
            
            if r - l + 1 == k:
                res.append(nums[dq[0]])
                l += 1
        
        return res