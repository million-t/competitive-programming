# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(str, input().split(' ')))
n = int(input())
ans = True
lengthOfA = len(A)
for i in range(n):
    anotherSet = set(map(str, input().split(' ')))
    if len(anotherSet) >= lengthOfA or not anotherSet.issubset(A):
        ans = False
        break
print(ans)
