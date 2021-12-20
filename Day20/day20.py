from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

if True:
    Filename = "Day20/input.txt"
else:
    Filename = "Day20/sample.txt"


bitmap = []
lightPixels = set({})
rowSize = 0
colSize = 0
with open(Filename) as f:
    line = f.readline().strip()
    for c in line:
        bitmap.append(str(int(c == "#")))
    line = f.readline().strip()
    row = 0
    while line := f.readline().strip():
        col = 0
        for c in line:
            if c == "#":
                lightPixels.add((row, col))
            col += 1
        row += 1
    rowSize, colSize = row, col

#print(lightPixels)
#print(rowSize, colSize)

steps = [
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,-1),
    (0,0),
    (0,1),
    (1,-1),
    (1,0),
    (1,1)
]


def part1():
    global rowSize, colSize, lightPixels
    localLightPixels = deepcopy(lightPixels)
    offGridPixels = "0"
    for _ in range(2):
        newLightPixels = set({})
        for row in range(rowSize+2):
            for col in range(colSize+2):
                binStr = ""
                for step in steps:
                    dRow, dCol = step
                    if (row+dRow-1, col+dCol-1) in localLightPixels:
                        binStr += "1"
                    elif rowSize > row+dRow-1 >= 0 and colSize > col+dCol-1 >= 0:
                        binStr += "0"
                    else:
                        binStr += str(offGridPixels)
                newLightPixels.add((row, col)) if int(bitmap[int(binStr, 2)]) else None
        localLightPixels = deepcopy(newLightPixels)

        # print(offGridPixels)
        rowSize += 2
        colSize += 2
        offGridPixels = bitmap[int(offGridPixels*9,2)]
    # print(offGridPixels)

    for row in range(rowSize):
        for col in range(colSize):
            if (row, col) in localLightPixels:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print(len(localLightPixels))

    return

def part2():
    global rowSize, colSize, lightPixels
    localLightPixels = deepcopy(lightPixels)
    offGridPixels = "0"
    for _ in range(50):
        newLightPixels = set({})
        for row in range(rowSize+2):
            for col in range(colSize+2):
                binStr = ""
                for step in steps:
                    dRow, dCol = step
                    if (row+dRow-1, col+dCol-1) in localLightPixels:
                        binStr += "1"
                    elif rowSize > row+dRow-1 >= 0 and colSize > col+dCol-1 >= 0:
                        binStr += "0"
                    else:
                        binStr += str(offGridPixels)
                newLightPixels.add((row, col)) if int(bitmap[int(binStr, 2)]) else None
        localLightPixels = deepcopy(newLightPixels)

        # print(offGridPixels)
        rowSize += 2
        colSize += 2
        offGridPixels = bitmap[int(offGridPixels*9,2)]
    # print(offGridPixels)

    for row in range(rowSize):
        for col in range(colSize):
            if (row, col) in localLightPixels:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print(len(localLightPixels))

    return

def main():
    part1()
    part2()
    pass

if __name__ == "__main__":
    main()