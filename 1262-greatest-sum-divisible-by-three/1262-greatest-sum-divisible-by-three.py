class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        two = []
        one = []
        ans = 0
        
        for num in nums:
            ans += num
            mod = num%3
            if mod == 2:
                two.append(num)
            
            elif mod == 1:
                one.append(num)
        
        one.sort()
        two.sort()
        
        tot_mod = ans%3
        if tot_mod == 1:
            if one:
                rem = one[0]
                if len(two) > 1:
                    rem = min(rem, two[0] + two[1])
                ans -= rem
            
            else:
                ans -= two[0] + two[1]
        
        elif tot_mod == 2:
            if two:
                rem = two[0]
                if len(one) > 1:
                    rem = min(rem, one[0] + one[1])
                ans -= rem
            else:
                ans -= one[0] + one[1]
                
            
        
        return ans