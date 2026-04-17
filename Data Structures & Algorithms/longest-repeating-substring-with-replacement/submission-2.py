class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        char_map = {}
        left = 0
        max_l = 0

        for i in range(len(s)):
            char_map[s[i]] = char_map.get(s[i],0) + 1
            max_freq = max(max_freq,char_map[s[i]])
            while i - left + 1 - max_freq > k:
                char_map[s[left]] -=1
                left += 1
            max_l = max(max_l, i - left + 1)
        
        return max_l
            

        