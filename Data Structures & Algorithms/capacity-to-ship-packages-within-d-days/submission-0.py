class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canship(cap):
            ships, curcap = 1, cap
            for w in weights:
                if curcap - w < 0:
                    if ships + 1 > days:
                        return False
                    ships += 1
                    curcap = cap
                    # new ship arrived when we do curcap = cap and ships += 1
                curcap -= w
            return True

        while l <= r:
            cap = l + (r - l) // 2
            if canship(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        
        return res
        