class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        while l<=r:
            if people[r]+people[l]<=limit:
                l+=1
            boats += 1
            r -= 1
        return boats



