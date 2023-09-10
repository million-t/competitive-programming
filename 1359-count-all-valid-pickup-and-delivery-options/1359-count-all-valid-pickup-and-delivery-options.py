class Solution:
    def countOrders(self, n: int) -> int:
        
        available_slots = 1
        prev_orders = 1
        mod = 10**9 + 7
        
        
        for num in range(1, n + 1):
            distribution = (available_slots*(available_slots + 1)//2)%mod
            prev_orders = (prev_orders*distribution)%mod
            available_slots += 2
        
        return prev_orders
        
        