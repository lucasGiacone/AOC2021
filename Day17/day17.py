from math import sqrt
from dataclasses import dataclass

if True:
    Filename = "Day17/input.txt"
else:
    Filename = "Day17/sample.txt"

x_min = 0
x_max = 0
y_min = 0
y_max = 0

with open(Filename) as f:
    line = f.readline()
    x, y = line.split(',')
    x = x.split('=')[1]
    y = y.split('=')[1]
    x_min, x_max = [int(i) for i in x.split('..')]
    y_min, y_max = [int(i) for i in y.split('..')]
print(x_min, x_max, y_min, y_max)

def getMinXSpeed(x_min):
    it = int(sqrt(x_min))
    while True:
        if ((it * (it + 1)) // 2) <= x_min:
            it += 1
        else:
            return it


def getPos(n):
    n = abs(n)
    return (n*(n+1))//2



@dataclass
class speed:
    value: int
    time : list

@dataclass
class speeds:
    x : int
    y : int

def part1():
    validXspeed = []
    minXspeed = getMinXSpeed(x_min)
    maxXspeed = x_max
    for i in range(minXspeed, maxXspeed + 1):
        soma = 0
        cnt = 0
        j = i
        timeRange = []
        while i > 0:
            cnt += 1
            soma += i
            i -= 1
            if soma >= x_min:
                if soma <= x_max:
                    timeRange.append(cnt)
                else:
                    break
        if i == 0:
            timeRange.append(-1)
        if timeRange:
            validXspeed.append(speed(j,timeRange))
    print(validXspeed)

    maxYvel = y_min-1
    print(getPos(maxYvel))


def getTimeByPoss(max_y):
    timeByPos = {}
    for i in range(y_min, 1-max_y):
        j = i
        pos = 0
        cnt = 0
        validTime = []
        while True:
            pos += j
            j -= 1
            cnt += 1
            if pos <= y_max:
                if pos >= y_min:
                    validTime.append(cnt)
                else:
                    break
        if validTime:
            timeByPos[i] = validTime
    return timeByPos


def part2():
    validXspeed = []
    minXspeed = getMinXSpeed(x_min)
    maxXspeed = x_max
    for i in range(minXspeed, maxXspeed + 1):
        soma = 0
        cnt = 0
        j = i
        timeRange = []
        while i > 0:
            cnt += 1
            soma += i
            i -= 1
            if soma >= x_min:
                if soma <= x_max:
                    timeRange.append(cnt)
                else:
                    break
        if i == 0:
            timeRange.append(-1)
        if timeRange:
            validXspeed.append(speed(j,timeRange))
    print(validXspeed)

    maxYvel = y_min+1
    
    timeByPoss = getTimeByPoss(maxYvel)

    count = 0
    validPosses = []
    for key, val in timeByPoss.items():
        for time in val:
            for s in validXspeed:
                if time in s.time:
                    val2 = [s.value, key]
                    if val2 not in validPosses:
                        validPosses.append(val2)
                    count += 1
                elif time > s.time[0] and s.time[-1] == -1:
                    count += 1
                    val2 = [s.value, key]
                    if val2 not in validPosses:
                        validPosses.append(val2)
    # for i in validPosses:
    #     print(i)
    print(len(validPosses))

    

def main():
    #part1()
    part2()


if __name__ == "__main__":
    main()