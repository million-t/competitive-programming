class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        letter = defaultdict(lambda :[0]*26)
        
        for vote in votes:
            for indx, char in enumerate(vote):
                letter[char][indx] -= 1
        
        
        return "".join(sorted(letter.keys(), key=lambda x: (letter[x], x)))