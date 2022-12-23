class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = 0
        for i, num in enumerate(num2[::-1]):
            summ = 0
            carry = 0
            j = 0
            for each in num1[::-1]:
                digitProduct = ((ord(num)-48)*(ord(each)-48) + carry)%10
                summ += (digitProduct)*10**j
                carry = ((ord(num)-48)*(ord(each)-48) + carry)//10
                j+=1
                
            if carry:
                summ += carry*(10**j)

            product += summ*(10**i)
        return str(product)




        
