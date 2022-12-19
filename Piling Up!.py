# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    blocks = list(map(int, input().split()))
    top = float('inf')
    l, r = 0, N-1
    while l<r and top>=max([blocks[l],blocks[r]]):
        if blocks[l]>= blocks[r]:
            top = blocks[l]
            l+=1
        else:
            top = blocks[r]
            r-=1
    ans.append('Yes') if l==r else ans.append('No')
for i in range(T):
    print(ans[i])
    
    
