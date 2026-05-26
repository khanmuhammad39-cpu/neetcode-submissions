class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numbers = set(nums)
        longest = 1
        for num in numbers:
            length = 1
            check_num = num
            while check_num+1 in nums:
                length += 1
                longest = max(longest,length)
                check_num = check_num + 1
        
        return longest