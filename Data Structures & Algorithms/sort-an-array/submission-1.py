class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left_sorted = self.sortArray(nums[:mid])
        right_sorted = self.sortArray(nums[mid:])

        return self.merge(left_sorted, right_sorted)

    def merge(self,left_sorted: List[int],right_sorted: List[int]) -> List[int]:
        i = j = 0
        res = []

        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] < right_sorted[j]:
                res.append(left_sorted[i])
                i += 1
            else:
                res.append(right_sorted[j])
                j += 1
        
        res.extend(left_sorted[i:])
        res.extend(right_sorted[j:])

        return res



