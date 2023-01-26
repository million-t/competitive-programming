t = int(input())

for _ in range(t):
    n = int(input())
    seq = list(map(int, input().split()))

    leftVal = seq[0]
    max_sum  = seq[0]

    for i in range(1, n):
        
        if leftVal*seq[i] > 0 and leftVal < seq[i]:        
            max_sum += seq[i] - leftVal
            leftVal = seq[i]
            
        elif leftVal*seq[i] < 0:
            leftVal = seq[i]
            max_sum += seq[i]
    
    print(max_sum)
