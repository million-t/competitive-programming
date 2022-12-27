class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}
        for cpd in cpdomains:
            arr = cpd.split(' ')
            domain = arr[1]
            
            right = len(domain)-1
            
            while right>=0:   
                while right >= 0 and domain[right] != '.':
                    right-=1
                count[domain[right + 1:]] = count.get(domain[right+1:], 0) + int(arr[0])                
                right -= 1
        ans = []
        for key, val in count.items():
            ans.append(str(val) + ' ' + str(key))
        return ans