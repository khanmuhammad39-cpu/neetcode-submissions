class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        req_len = n//3
        cand_1, cand_2 = None, None
        count_1,count_2 = 0,0

        for i in range(n):
            num = nums[i]
            if num == cand_1:
                count_1 += 1
            elif num == cand_2:
                count_2 += 1
            elif count_1 == 0:
                cand_1 = num
                count_1 = 1
            elif count_2 == 0:
                cand_2 = num
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1
        
        count_1, count_2 = 0,0
        for i in range(n):
            if nums[i] == cand_1:
                count_1 += 1
            elif nums[i] == cand_2:
                count_2 += 1
            else:
                continue
        
        if count_1 > req_len and count_2 > req_len:
            return [cand_1,cand_2]
        elif count_1 > req_len and count_2 <= req_len:
            return [cand_1]
        elif count_1 <= req_len and count_2 > req_len:
            return [cand_2]
        else:
            return []

            