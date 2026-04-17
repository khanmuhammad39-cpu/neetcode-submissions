class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for words in strs:
            sorted_word = "".join(sorted(list(words)))
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []
                anagram_map[sorted_word].append(words)
            else:
                anagram_map[sorted_word].append(words)

        
        return list(anagram_map.values())
    
            
        