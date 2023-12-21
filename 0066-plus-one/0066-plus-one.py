class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits.reverse()
        carry = 1
        
        for indx, dig in enumerate(digits):
            if carry + dig > 9:
                digits[indx] = 0
            
            else:
                digits[indx] += carry
                carry = 0
        
        if carry:
            digits.append(carry)
        
        digits.reverse()
        return digits
        
        