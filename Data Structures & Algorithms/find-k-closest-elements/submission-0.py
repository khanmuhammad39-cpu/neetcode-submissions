class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        
        left = 0
        right = k - 1
        best_window = float('inf')
        best_left = 0

        while right < len(arr):
            sum_difference = 0
            for i in range(left,right+1,1):
                sum_difference += abs(x-arr[i])
            if sum_difference < best_window:
                best_left = left
                best_window = sum_difference
            left += 1
            right += 1
        
        return arr[best_left:best_left+k]

        

        
