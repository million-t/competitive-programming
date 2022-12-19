# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
count = {}
for _ in range(n):
    wrd = input()
    count[wrd] = count.get(wrd, 0) + 1
print(len(count))
print(' '.join(map(str, list(count.values()))))
    
