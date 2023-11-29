class Solution:
    def hammingWeight(self, n: int) -> int:
        and_op_count = 0
        
        while n:
            n &= (n - 1)
            and_op_count += 1
        
        return and_op_count