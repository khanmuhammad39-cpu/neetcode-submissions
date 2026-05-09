class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys_4_map = []

        for i in range(len(strs)):
            cur_sorted_word = sorted(strs[i])
            keys_4_map.append("".join(cur_sorted_word))
        
        hashmap = {}

        for i in range(len(keys_4_map)):
            if keys_4_map[i] not in hashmap:
                hashmap[keys_4_map[i]] = []
        
        keys_4_map = []

        for s in strs:
            sorted_word = "".join(sorted(s))
            hashmap[sorted_word].append(s)

        return list(hashmap.values())