class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        #split the real and imaginary parts for each number
        real1, imgnry1 = num1.split('+')
        real2, imgnry2 = num2.split('+')
        # cast the string numbers into int type
        real1 = int(real1)
        real2 = int(real2)
        imgnry1 = int(imgnry1[:-1]) #sliced to remove 'i'
        imgnry2 = int(imgnry2[:-1])

        #perform the multiplication and cast back into str
        real_product = str(real1*real2 - (imgnry1*imgnry2))
        imgnry_product = [str(real1*imgnry2 + real2*imgnry1), 'i']
        imgnry_product = ''.join(imgnry_product)
        #use list to avoid string concatination which is considered less efficient 
        product = [real_product, imgnry_product]
        return '+'.join(product)

