def swapSide(side):
    if side == 'left':
        side = 'right'
    else:
        side = 'left'
    return side
    
c = int(input())
while c:
    allCars = []
    cap, travelTime, numOfCars = map(int, input().split(" "))

    for i in range(numOfCars):
        arrv, side = input().split(' ')
        arrv = int(arrv)
        allCars.append([i, arrv, side])
    
    time = 0
    
    banksData = dict()
    banksData['left'] = []
    banksData['right'] = []
    
    carsOnFerry = []
    side = 'left'
    allTimes = [None] * len(allCars)
    
    while (len(allCars)>0 or len(banksData['left'])>0 or len(banksData['right'])>0):
        for car in allCars[:]:
            if (car[1]>time):
                break
            else:
                banksData[car[2]].append(car)
                allCars.remove(car)
    
        if (len(carsOnFerry)<cap and len(banksData[side])>0):
            if ((len(banksData[side]) + len(carsOnFerry))<=cap):
                for car in banksData[side]:
                    carsOnFerry.append(car[0])
                banksData[side] = []
            else:
                capLeft = cap - len(carsOnFerry)
                for car in banksData[side][:capLeft]:
                    carsOnFerry.append(car[0])
                banksData[side] = banksData[side][capLeft:]
    
        if (len(carsOnFerry)>0 or len(banksData['left'])>0 or len(banksData['right'])>0):
            side = swapSide(side)
            time = time + travelTime
            for i in carsOnFerry:
                allTimes[i] = time
            carsOnFerry = []
        elif (len(allCars)>0):
            nxt = allCars[0][1]
            time = time + (nxt - time)
    
    for t in allTimes:
        print(t)
    print()
    c = c-1