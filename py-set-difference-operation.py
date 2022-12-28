# Enter your code here. Read input from STDIN. Print output to STDOUT
numEnglishPupil = int(input())
subscribedToEnglish = set(input().split(' '))
numFrenchPupil = int(input())
subscribedToFrench = set(input().split(' '))
print(len(subscribedToEnglish.difference(subscribedToFrench)))
