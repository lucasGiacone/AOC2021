from dataclasses import dataclass
import math

if True:
    Filename = "Day14/input.txt"
else:
    Filename = "Day14/sample.txt"


line = ""
first = ""
last = ""
charMap = {}
step = {}
quants = {}
with open(Filename) as f:
    line = f.readline().strip()
    first = line[0]
    last = line[-1]
    _ = f.readline()
    inst = f.readline().strip()
    while inst:
        origin, end = inst.split(" -> ")
        for c in origin:
            if c not in quants:
                quants[c] = 0

        charMap[origin] = [f"{origin[0]+end}",f"{end+origin[-1]}"]
        step[origin] = 0
        inst = f.readline().strip()
    for idx in range(len(line)-1):
        base = line[idx]+line[idx+1]
        step[base] += 1
quants[first] += 1
quants[last] += 1
#print(charMap)
print(quants)
#print(step)




def part1():
    global step
    global quants
    for _ in range(10):
        newDict = {}
        for k in charMap:
            newDict[k] = 0
        for key, value in step.items():
            newKeys = charMap[key]
            for newKey in newKeys:
                newDict[newKey] += value
        step = newDict

    for k, v in step.items():
        for c in k:
            quants[c] += v

    for k, v in quants.items():
        quants[k] = v // 2

    print(quants)

def part2():
    global step
    global quants
    for _ in range(40):
        newDict = {}
        for k in charMap:
            newDict[k] = 0
        for key, value in step.items():
            newKeys = charMap[key]
            for newKey in newKeys:
                newDict[newKey] += value
        step = newDict

    for k, v in step.items():
        for c in k:
            quants[c] += v

    maxi = 0
    mini = math.inf
    for k, v in quants.items():
        quants[k] = v // 2
        if v // 2 > maxi:
            maxi = v // 2
        if v // 2 < mini:
            mini = v // 2

    print(quants)
    print(maxi)
    print(mini)
    print(maxi-mini)
    pass


def main():
    #part1()
    part2()


if __name__ == "__main__":
    main()