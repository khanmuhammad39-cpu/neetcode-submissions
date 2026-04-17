class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                skipL = s[left+1:right+1]
                skipR = s[left:right]
                return skipL == s[right:left:-1] or skipR == s[right-1:left-1:-1]
        
        return True
        