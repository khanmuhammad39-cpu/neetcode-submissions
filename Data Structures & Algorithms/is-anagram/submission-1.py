class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_map = {}

        for char in s:
            anagram_map[char] = anagram_map.get(char,0) + 1

        for char in t:
            if char not in anagram_map:
                return False
            anagram_map[char] = anagram_map.get(char) - 1
            
        for key, value in anagram_map.items():
            if value != 0:
                return False
            
        
        return True
        

        

        