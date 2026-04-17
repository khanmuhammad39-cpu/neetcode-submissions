class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        counter = 0

        while l < r:
            if people[r] + people[l] <= limit:
                counter += 1
                l += 1
                r -= 1
            else:
                counter += 1
                r -= 1
        
        return counter + 1 if l == r else counter
        