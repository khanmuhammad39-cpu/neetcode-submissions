class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        
        for idx, words in enumerate(strs):
            chunk = str(len(words))+'#'+words
            encoded_str.append(chunk)
        
        final = "".join(encoded_str)

        return final


    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        res = []
        # 5#Hello5#World
        while i < len(s):

            while s[j].isdigit():
                j+=1
            
            L = int(s[i:j])
            res.append(s[j+1:j+L+1])
            j = j + L + 1
            i = j
        
        return res



            
