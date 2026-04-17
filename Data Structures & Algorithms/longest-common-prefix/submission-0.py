class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for i,words in enumerate(strs):
            if i==0:
                continue
            if words == res:
                continue
            j = 0
            while j<len(words) and j<len(res) and res[j] == words[j]:
                j +=1
            res = res[:j]
        
        return res

