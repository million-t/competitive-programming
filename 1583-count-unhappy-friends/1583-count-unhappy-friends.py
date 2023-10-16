class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        
        preference = [defaultdict(int) for person in range(n)]
        pair = {}
        
        for person in range(n):
            for indx, another in enumerate(preferences[person]):
                preference[person][another] = indx
        
        for a, b in pairs:
            pair[a] = b
            pair[b] = a
        
        unhappy = 0
        for a in pair:
            b = pair[a]
            
            for friend in preferences[a]:
                if friend == b:
                    break
                
                if preference[friend][a] < preference[friend][pair[friend]]:
                    unhappy += 1
                    break
            
        
        return unhappy
            
        
                
        
        