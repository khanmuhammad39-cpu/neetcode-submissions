class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("infinity")

        for i in range(len(strs)):
            if len(strs[i]) <= min_length:
                min_length = len(strs[i])
        
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        
        return strs[0][:min_length]


            

        