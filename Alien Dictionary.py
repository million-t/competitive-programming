#User function Template for python3
from collections import defaultdict, deque

class Solution:
    def findOrder(self,alien_dict, N, K):
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for word in alien_dict:
            for char in word:
                if not graph[char]:
                    graph[char] = []
        
        
        
        for ind in range(1, N):
            
            i = 0
            word1 = alien_dict[ind - 1]
            word2 = alien_dict[ind]
            while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
                i += 1
            
            if i < len(word1) and i < len(word2):
                graph[word1[i]].append(word2[i])
                indegree[word2[i]] += 1
            
            elif len(word1) > len(word2):
                return ''
        
        queue = deque()
        
        for node in graph:
            if not indegree[node]:
                queue.append(node)
        
        order = []
        while queue:
            cur = queue.popleft()
            
            order.append(cur)
            
            for neigh in graph[cur]:
                indegree[neigh] -= 1
                
                if not indegree[neigh]:
                    queue.append(neigh)
        
        if len(order) == K:
            return ''.join(order)
        
        
        return ''
            
        
            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
