class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            area = (r-l)*min(heights[l],heights[r])
            max_area = max(max_area,area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                if heights [l+1] > heights [r-1]:
                    l += 1
                else:
                    r -= 1
        
        return max_area

            
        