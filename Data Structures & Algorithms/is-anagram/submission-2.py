class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_map = {}
        anagram_map2 = {}

        for chars in s:
            anagram_map[chars] = anagram_map.get(chars,0) + 1
        
        for char in t:
            anagram_map2[char] = anagram_map2.get(char,0) + 1

        if anagram_map2 != anagram_map:
            return False
        
        return True
        
