class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        # constructing flights
        flights = [0]*(n + 1)
        
        # handle edges of the booking ranges
        for first, last, seats in bookings:
            flights[first - 1] += seats
            flights[last] -= seats
        
        # building the prefix sum array
        for indx in range(1, n + 1):
            flights[indx] += flights[indx - 1]
        
        flights.pop()
        return flights
        