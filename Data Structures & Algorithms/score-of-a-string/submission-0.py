class Solution:
    def scoreOfString(self, s: str) -> int:
        running_sum = 0
        for i in range(len(s)):
            if i == 0:
                continue
            running_sum += abs(ord(s[i]) - ord(s[i - 1]))
        return running_sum


        