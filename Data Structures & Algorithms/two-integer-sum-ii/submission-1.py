class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = i + 1

        while j < len(numbers):
            if numbers[i] + numbers[len(numbers)-1] < target:
                i += 1
            targetcheck = numbers[i] + numbers[j]
            if targetcheck < target:
                j += 1
            elif targetcheck == target:
                return [i+1,j+1]
            else:
                i += 1
                j = i + 1
        
        return []

        