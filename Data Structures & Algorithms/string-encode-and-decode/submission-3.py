class Solution:
# 5#Hello5#World
    def encode(self, strs: List[str]) -> str:
        encoded_word = ""

        for word in strs:
            encoded_word = encoded_word + str(len(word)) + "#" + word
        
        return encoded_word

    def decode(self, s: str) -> List[str]:
        words = []
        i,j = 0,0
        while i < len(s):
            while s[j] != "#":
                j += 1
            
            len_word = int(s[i:j])
            words.append(s[j+1:j+len_word+1])
            
            j = j + 1 + len_word
            i = j
        
        return words


            
        



