tests = int(input())

for test in range(tests):
    a, b = list(map(int, input().split()))

    start = 0
    end = (a + b)//4
    
    max_teams = 0

    while start <= end:
        mid = start + (end - start)//2

        if a >= mid and b >= mid and 4*mid <= a + b:
            max_teams = mid
            start = mid + 1
        
        else:
            end = mid - 1
    
    print(max_teams)
