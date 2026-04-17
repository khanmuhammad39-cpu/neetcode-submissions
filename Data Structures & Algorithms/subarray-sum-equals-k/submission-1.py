class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {}
        prefix_map[0] = 1
        counter = 0
        pref_sum = 0

        for i in range(len(nums)):
            pref_sum += nums[i]
            need = pref_sum - k
            if need in prefix_map:
                counter += prefix_map.get(need)
            prefix_map[pref_sum] = prefix_map.get(pref_sum,0) + 1

        return counter

        



        

             
        