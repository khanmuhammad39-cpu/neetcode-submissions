class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        char_map = {}
        max_char = 0
        longest = 0
        char_map[s[left]] = char_map.get(s[left],0) + 1

        for i in range(1,len(s)):
            char_map[s[i]] = char_map.get(s[i],0) + 1
            max_char = max(max_char,char_map[s[i]])
            window_size = i - left + 1
            if window_size - max_char > k:
                char_map[s[left]] -= 1
                left += 1
            else:
                longest = max(longest,window_size)
            
        return longest



            
             
            