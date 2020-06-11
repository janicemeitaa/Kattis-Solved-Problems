import sys
for i in sys.stdin:
    idx = 1
    for k in i:
        if (k=='A'):
            # Swap ball from 1 to 2
            if (idx==1):
                idx = 2
            elif (idx==2):
                idx = 1
            else:
                continue
        elif (k=='B'):
            # Swap ball from 2 to 3
            if (idx==2):
                idx = 3
            elif (idx==3):
                idx = 2
            else:
                continue
        elif (k=='C'):
            # Swap ball from 1 to 3
            if (idx==1):
                idx = 3
            elif (idx==3):
                idx = 1
            else:
                continue
    print(idx)
