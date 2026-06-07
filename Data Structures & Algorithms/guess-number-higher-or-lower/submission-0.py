class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            m = (l + r) // 2
            res = guess(m)        # guess the midpoint
            if res == 0:
                return m          # correct guess
            elif res == -1:
                r = m - 1         # too high, go left
            else:
                l = m + 1         # too low, go right