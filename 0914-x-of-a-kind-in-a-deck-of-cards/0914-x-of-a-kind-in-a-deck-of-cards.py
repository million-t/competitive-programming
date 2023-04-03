class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        def gcd(a, b):
            if not b:
                return a
            
            return gcd(b, a%b)
        
        
        _gcd = 0
        for count in Counter(deck).values():
            _gcd = gcd(count, _gcd)
        
        return _gcd > 1
        