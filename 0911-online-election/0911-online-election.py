class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.votes = defaultdict(int)
        self.lead = [0]*len(times)
        self.times = times
        
        leading_vote = 0
        for i, person in enumerate(persons):
            
            self.votes[person] += 1
            
            if self.votes[person] >= leading_vote:
                self.lead[i] = person
                leading_vote = self.votes[person]
                
            else:
                self.lead[i] = self.lead[i - 1]
                
        
    def q(self, t: int) -> int:
        
        start = 0
        end = len(self.times) - 1
        
        while start <= end:
            mid = start + (end - start)//2
            
            if self.times[mid] <= t:
                start = mid + 1
            
            else:
                end = mid - 1
        
        return self.lead[start - 1]
        
        # return self.lead[bisect_right(self.times, t) - 1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)