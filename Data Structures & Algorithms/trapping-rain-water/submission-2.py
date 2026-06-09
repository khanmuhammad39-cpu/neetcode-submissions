class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxl = height[l]
        maxr = height[r]
        res = 0

        while l < r:
            if maxl <= maxr:
                #bottle neck is left
                l += 1
                if maxl >= height[l]:
                    res += maxl - height[l]
                maxl = max(maxl,height[l])
            else:
                r -= 1
                if maxr >= height[r]:
                    res += maxr - height[r]
                maxr = max(maxr,height[r])
                
        return res
        