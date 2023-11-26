class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = 0
        cows = 0
        s_seen, g_seen = defaultdict(int), defaultdict(int)
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            
            else:
                s_seen[s] += 1
                g_seen[g] += 1
        
        
        for dig in g_seen:
            cows += min(s_seen[dig], g_seen[dig])    
        
        return f"{bulls}A{cows}B"