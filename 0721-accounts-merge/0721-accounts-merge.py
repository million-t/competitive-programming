class DSU:
    def __init__(self, words):
        
        self.rep = {word: word for word in words}
        self.rank = {word: 1 for word in words}
    
    def find(self, x):
        
        root = x
        while root != self.rep[root]:
            root = self.rep[root]
        
        while x != root:
            temp = self.rep[x]
            self.rep[x] = root
            x = temp
        
        return root
    
    def union(self, x, y):
        rep_x = self.find(x)
        rep_y = self.find(y)
        
        if rep_x == rep_y:
            return
        
        if self.rank[rep_x] > self.rank[rep_y]:
            self.rep[rep_y] = rep_x
        
        elif self.rank[rep_x] < self.rank[rep_y]:
            self.rep[rep_x] = rep_y
        
        else:
            self.rep[rep_y] = rep_x
            self.rank[rep_x] += 1
        
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        email_name = {}
        emails = set()
        
        for account in accounts:
            
            name = account[0]
            for ind in range(1, len(account)):
                email = account[ind]
                email_name[email] = name
                emails.add(email)
        
        
        union_find = DSU(emails)
        for account in accounts:
            
            email1 = account[1]
            for ind in range(2, len(account)):
                union_find.union(email1, account[ind])
        
        rep_emails = defaultdict(list)
        for email in emails:
            rep_emails[union_find.find(email)].append(email)
        
        
        ans = []
        for rep, cur_emails in rep_emails.items():
            cur_emails.sort()
            
            ans.append([email_name[rep]] + cur_emails)
        
        return ans
            
        
        
        
                
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        