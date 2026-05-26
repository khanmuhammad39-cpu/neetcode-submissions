class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numbers = set(nums)
        longest = 0
        for num in numbers:
            if num - 1 not in numbers:
                length = 1
                check_num = num
                while check_num + 1 in numbers:
                    length += 1
                    check_num = check_num + 1
                longest = max(longest,length)
        
        return longest