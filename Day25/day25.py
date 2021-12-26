from collections import deque
from copy import deepcopy as dp

if True:
    Filename = "Day25/input.txt"
else:
    Filename = "Day25/sample.txt"

def parseInput(filename):
    rightMovers = []
    downMovers  = []
    with open(filename) as f:
        lineIdx = 0
        while line := f.readline():
            line = line.strip()
            rightMoverLine = deque()
            downMoverCol = deque()
            if lineIdx == 0:
                for _ in line:
                    downMovers.append(deque())

            for charIdx, char in enumerate(line):
                if char == ">":
                    rightMoverLine.append(charIdx)
                elif char == "v":
                    downMoverCol.append(charIdx)
            rightMovers.append(rightMoverLine)
            for col in downMoverCol:
                downMovers[col].append(lineIdx)
            lineIdx += 1
    # printBoard(rightMovers, downMovers)
    return (rightMovers, downMovers)
            
def printBoard(rightMovers, downMovers):
    for i in range(len(rightMovers)):
        for j in range(len(downMovers)):
            if j in rightMovers[i]:
                print(">", end="")
            elif i in downMovers[j]:
                print("v", end="")
            else:
                print(".", end="")
        print()
    print()
    
def part1(parseInput):
    rightMovers, downMovers = parseInput
    move = True
    steps = 0
    while move:
        move = False
        rightMoversSet = [set(rightMover) for rightMover in rightMovers]
        downMoversSet = [set(downMover) for downMover in downMovers]

        newRightMovers = dp(rightMovers)
        newRightMoversSet = dp(rightMoversSet)

        height = len(rightMovers)
        width = len(downMovers)

        for lineIdx, line in enumerate(rightMovers):
            for idx, col in enumerate(line):
                if idx != len(line) - 1:
                    if line[idx + 1] != col + 1 and lineIdx not in downMoversSet[col+1]:
                        move = True
                        newRightMovers[lineIdx][idx] += 1
                        newRightMoversSet[lineIdx].remove(col)
                        newRightMoversSet[lineIdx].add(col+1)
                elif col == width - 1:
                    if line[0] != 0 and lineIdx not in downMoversSet[0]:
                        move = True
                        newRightMoversSet[lineIdx].remove(col)
                        newRightMoversSet[lineIdx].add(0)
                        newRightMovers[lineIdx].pop()
                        newRightMovers[lineIdx].appendleft(0)
                else:
                    if lineIdx not in downMoversSet[col+1]:
                        move = True
                        newRightMoversSet[lineIdx].remove(col)
                        newRightMoversSet[lineIdx].add(col+1)
                        newRightMovers[lineIdx][idx] += 1
        
        rightMovers = newRightMovers
        rightMoversSet = newRightMoversSet

        newDownMovers = dp(downMovers)
        newDownMoversSet = dp(downMoversSet)            


        for colIdx, col in enumerate(downMovers):
            for idx, line in enumerate(col):
                if idx != len(col) - 1:
                    if col[idx + 1] != line + 1 and colIdx not in rightMoversSet[line+1]:
                        move = True
                        newDownMovers[colIdx][idx] += 1
                        newDownMoversSet[colIdx].remove(line)
                        newDownMoversSet[colIdx].add(line+1)
                elif line == height - 1:
                    if col[0] != 0 and colIdx not in rightMoversSet[0]:
                        move = True
                        newDownMoversSet[colIdx].remove(line)
                        newDownMoversSet[colIdx].add(0)
                        newDownMovers[colIdx].pop()
                        newDownMovers[colIdx].appendleft(0)
                else:
                    if colIdx not in rightMoversSet[line+1]:
                        move = True
                        newDownMoversSet[colIdx].remove(line)
                        newDownMoversSet[colIdx].add(line+1)
                        newDownMovers[colIdx][idx] += 1
        
        downMovers = newDownMovers
        downMoversSet = newDownMoversSet
        steps+=1
        # if steps > 100:
        #     break
    print(steps)
    # printBoard(rightMovers, downMovers)
                

def main():
    parsedInput = parseInput(Filename)
    part1(parsedInput)
    # part2(parsedInput)
    pass

if __name__ == "__main__":
    main()