class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT = {}
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        l = 0
        resLen = float("inf")
        res = [-1,-1]
        window = {}
        have = 0
        need = len(countT)

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l,r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1 
        return s[res[0]:res[1] + 1] if resLen != float("infinity") else ""
                
                