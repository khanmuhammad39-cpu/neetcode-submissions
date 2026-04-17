class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_l = 0
        max_r = 0
        water = 0

        while l < r:
            if height[l] < height[r]:
                if max_l < height[l]:
                    l += 1
                    max_l = height[l-1]
                    continue
                else:
                    water += (max_l - height[l])
                    l += 1
            else:
                if max_r < height[r]:
                    r -= 1
                    max_r = height[r+1]
                else:
                    water += (max_r - height[r])
                    r -= 1
        
        return water
                    

        