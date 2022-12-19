# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
rooms = input().split(' ')
count = {}
for r in rooms:
    count[r] = count.get(r, 0) + 1
for key in count.keys():
    if count[key] == 1:
        print(key)
        break
