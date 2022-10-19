class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0]*(n+1)
        for x, y, z in bookings:
            prefix[x-1] += z
            prefix[y] -= z
        p = prefix[0]
        for i in range(1, n):
            p+=prefix[i]
            prefix[i] = p
        return prefix[:-1]

        
            
