class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for s in strs:
            sorted_current = "".join(sorted(s))
            if sorted_current not in hashmap:
                hashmap[sorted_current] = []
            
            hashmap[sorted_current].append(s)
            
        return list(hashmap.values())       