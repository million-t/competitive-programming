# Enter your code here. Read input from STDIN. Print output to STDOUT
sizes = input().split(' ')
arr = input().split(' ')
A = input().split(' ')
B = input().split(' ')

happy = 0
count = {}
for num in arr:
    count[num] = count.get(num, 0) + 1
for num in A:
    happy += count.get(num, 0)
for num in B:
    happy -= count.get(num, 0)
print(happy)
    
