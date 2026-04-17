class Solution:
    
    def __init__(self):
        self.encode_word = None

    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            word_list = list(word)
            len_word = str(len(word_list))
            encoded_word = len_word + "#" + "".join(word_list)
            res.append(encoded_word)
        
        encode = "".join(res)
        self.encode_word = encode

        return encode
    
    def decode(self, s: str) -> List[str]:
        num_list = ["0","1","2","3","4","5","6","7","8","9"]
        res = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length

        return res
                    

