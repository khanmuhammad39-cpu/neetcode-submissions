class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        char_map = {}
        max_length = 0

        for i, char in enumerate(s):
            char_map[char] = char_map.get(char,0) + 1
            max_freq = max(max_freq,char_map[char])
            while i - left + 1 - max_freq > k:
                char_map[s[left]] -= 1
                left += 1
            max_length = max(max_length, i - left + 1)
        
        return max_length


            
            


        