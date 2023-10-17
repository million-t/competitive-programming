class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        
        n = 366
        day = [float('inf')]*n
        week = [float('inf')]*n
        month = [float('inf')]*n
        
        days.reverse()
        
        prev_val = 0
        while days:
            cur_day = days.pop()
            
            day[cur_day] = prev_val + min(day[cur_day], costs[0])
            
            
            for we_day in range(cur_day, min(n, cur_day + 7)):
                week[we_day] = min(week[we_day], prev_val + costs[1])
            
            for month_day in range(cur_day, min(n, cur_day + 30)):
                month[month_day] = min(month[month_day], prev_val + costs[2])
            
            prev_val = min(day[cur_day], week[cur_day], month[cur_day])
            

        return prev_val
            
            
            
            
            
        
        
        
        
#         @cache
#         def dp(indx, left):
            
            
#             if indx == len(days) - 1:
#                 return min(costs) if not left else 0
            
#             ans = float('inf')
#             if left > 0:
#                 ans = dp(indx + 1, max(0, left - (days[indx + 1] - days[indx])))
                
#             ans = min(ans, dp(indx + 1, 0) + costs[0],
#                             dp(indx + 1, max(0, 7 - (days[indx + 1] - days[indx]))) + costs[1],
#                             dp(indx + 1, max(0, 30 - (days[indx + 1] - days[indx]))) + costs[2])
            
#             return ans
        
#         return dp(0, 0)
                
        