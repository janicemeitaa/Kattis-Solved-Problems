n = int(input())
t = [int(i) for i in input().split()]
negCount = 0

for i in range(n):
    if (t[i] < 0):
        negCount += 1
    pass

print(negCount)