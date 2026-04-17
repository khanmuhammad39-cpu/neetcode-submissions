class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        anagram_map = {}

        for char in s:
            anagram_map[char] = anagram_map.get(char,0) + 1
        
        for char in t:
            if char not in anagram_map:
                return False
            anagram_map[char] -= 1
            if anagram_map[char] == 0:
                del anagram_map[char]
        
        return True

        