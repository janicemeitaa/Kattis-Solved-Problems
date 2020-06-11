import sys
n = 1
for i in sys.stdin:
    inputstr = i.split()
    
    # 1st line of input
    if (n == 1):
        cap = int(inputstr[0])
        part = int(inputstr[1])
        n+=1
        continue

    # 2nd line of input
    if (n == 2):
        # Boolean array, if width is feasible = True, and vice versa
        checkWidth = [0 for x in range(cap+1)]
        # Array storing all the partitions
        allBorders = []
        # Max capacity always feasible
        checkWidth[cap] = True
        
        # Reading all partition numbers
        for j in range(part):
            border = int(inputstr[j])
            allBorders.append(border)
            # Width in between partition and capacity is feasible
            checkWidth[border] = True
            checkWidth[cap-border] = True
        # Width in between partitions is feasible
        for j in range(part):
            for k in range(j+1, part):
                checkWidth[allBorders[k]-allBorders[j]] = True
        # Print all feasible widths
        for j in range(cap+1):
            if (checkWidth[j] == True):
                print(j, end = " ")
            
