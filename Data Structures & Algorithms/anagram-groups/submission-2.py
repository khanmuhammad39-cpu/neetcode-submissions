class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for words in strs:
            index_list = [0 for i in range(26)]
            for char in words:
                idx = ord(char) - ord('a')
                index_list[idx] += 1
            
            key = tuple(index_list)
            if key not in anagram_map:
                anagram_map[key] = []
                anagram_map[key].append(words)
            else:
                anagram_map[key].append(words)
        
        return list(anagram_map.values())

        
        