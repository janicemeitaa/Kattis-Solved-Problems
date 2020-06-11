n = int(input())
bus = [int(x) for x in input().split()]
tmp = []

busSorted = sorted(bus)

c = 0
while (c<n):
  i = c
  while ((i<n-1) and (busSorted[i+1] == busSorted[i]+1)):
    i = i+1
  if (c >= i-1):
    tmp.append(str(busSorted[c]))
    c = c+1
  else:
    tmp.append(str('{}-{}'.format(busSorted[c], busSorted[i])))
    c = i+1
print(' '.join(tmp))