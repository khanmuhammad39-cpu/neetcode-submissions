class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        s = []

        while i < len(word1) and j < len(word2):
            s.append(word1[i])
            s.append(word2[j])
            i += 1
            j += 1
            
        s.append(word1[i:])
        s.append(word2[j:])

        return "".join(s)

        