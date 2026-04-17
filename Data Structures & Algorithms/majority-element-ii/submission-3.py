class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        req_len = n // 3

        cand_1 = cand_2 = None
        count_1 = count_2 = 0

        # Phase 1: find up to two candidates
        for num in nums:
            if cand_1 == num:
                count_1 += 1
            elif cand_2 == num:
                count_2 += 1
            elif count_1 == 0:
                cand_1, count_1 = num, 1
            elif count_2 == 0:
                cand_2, count_2 = num, 1
            else:
                count_1 -= 1
                count_2 -= 1

        # Phase 2: verify actual frequencies
        freq_1 = freq_2 = 0
        for num in nums:
            if num == cand_1:
                freq_1 += 1
            elif num == cand_2:
                freq_2 += 1

        res = []
        if freq_1 > req_len:
            res.append(cand_1)
        if cand_2 is not None and cand_2 != cand_1 and freq_2 > req_len:
            res.append(cand_2)

        return res
        