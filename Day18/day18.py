import json
import copy
from math import ceil, floor
from dataclasses import dataclass

if True:
    Filename = "Day18/input.txt"
else:
    Filename = "Day18/sample.txt"

numbers = []

with open(Filename) as f:
    for line in f:
        numbers.append(json.loads(line))

# for n in numbers:
#     print(n)


def explode(number, idx,jdx,kdx,ldx):
    # print(f"Exploding: {number[idx][jdx][kdx][ldx]}")
    # print(number)
    if ldx == 0:
        if kdx == 0:
            if jdx == 0:
                if idx == 0:
                    #faz nada
                    pass
                else:
                    if isinstance(number[idx-1], int):
                        number[idx-1] += number[idx][jdx][kdx][ldx][0]
                    elif isinstance(number[idx-1][-1], int):
                        number[idx-1][-1] += number[idx][jdx][kdx][ldx][0]
                    elif isinstance(number[idx-1][-1][-1], int):
                        number[idx-1][-1][-1] += number[idx][jdx][kdx][ldx][0]
                    else :
                        number[idx-1][-1][-1][-1] += number[idx][jdx][kdx][ldx][0]
            else:
                if isinstance(number[idx][jdx-1], int):
                    number[idx][jdx-1] += number[idx][jdx][kdx][ldx][0]
                elif isinstance(number[idx][jdx-1][-1], int):
                    number[idx][jdx-1][-1] += number[idx][jdx][kdx][ldx][0]
                else:
                    number[idx][jdx-1][-1][-1] += number[idx][jdx][kdx][ldx][0]
        else:
            if isinstance(number[idx][jdx][kdx-1], int):
                number[idx][jdx][kdx-1] += number[idx][jdx][kdx][ldx][0]
            else:
                number[idx][jdx][kdx-1][-1] += number[idx][jdx][kdx][ldx][0]
    else:
        number[idx][jdx][kdx][ldx-1] += number[idx][jdx][kdx][ldx][0]

    if ldx == len(number[idx][jdx][kdx])-1:
        if kdx == len(number[idx][jdx])-1:
            if jdx == len(number[idx])-1:
                if idx == len(number)-1:
                    #faz nada
                    pass
                else:
                    if isinstance(number[idx-1], int):
                        number[idx-1] += number[idx][jdx][kdx][ldx][1]
                    elif isinstance(number[idx-1][0], int):
                        number[idx-1][0] += number[idx][jdx][kdx][ldx][1]
                    elif isinstance(number[idx-1][0][0], int):
                        number[idx-1][0][0] += number[idx][jdx][kdx][ldx][1]
                    elif isinstance(number[idx-1][0][0][0], int):
                        number[idx-1][0][0][0] += number[idx][jdx][kdx][ldx][1]
                    else:
                        number[idx-1][0][0][0][0] += number[idx][jdx][kdx][ldx][1]
            else:
                if isinstance(number[idx][jdx-1], int):
                    number[idx][jdx-1] += number[idx][jdx][kdx][ldx][1]
                elif isinstance(number[idx][jdx-1][0], int):
                    number[idx][jdx-1][0] += number[idx][jdx][kdx][ldx][1]
                elif isinstance(number[idx][jdx-1][0][0], int):
                    number[idx][jdx-1][0][0] += number[idx][jdx][kdx][ldx][1]
                else:
                    number[idx][jdx-1][0][0][0] += number[idx][jdx][kdx][ldx][1]
        else:
            if isinstance(number[idx][jdx][kdx-1], int):
                number[idx][jdx][kdx-1] += number[idx][jdx][kdx][ldx][1]
            elif isinstance(number[idx][jdx][kdx-1][0], int):
                number[idx][jdx][kdx-1][0] += number[idx][jdx][kdx][ldx][1]
            else:
                number[idx][jdx][kdx-1][0][0] += number[idx][jdx][kdx][ldx][1]
    else:
        if isinstance(number[idx][jdx][kdx][ldx-1], int):
            number[idx][jdx][kdx][ldx-1] += number[idx][jdx][kdx][ldx][1]
        else:
            number[idx][jdx][kdx][ldx-1][0] += number[idx][jdx][kdx][ldx][1]
    number[idx][jdx][kdx][ldx] = 0
    # print(f"result:\n{number}")

def split(number, idx, jdx, kdx, ldx):
    if jdx == None:
        val = number[idx]
    elif kdx == None:
        val = number[idx][jdx]
    elif ldx == None:
        val = number[idx][jdx][kdx]
    else:
        val = number[idx][jdx][kdx][ldx]
    val1 = floor(val/2)
    val2 = ceil(val/2)
    if jdx == None:
        number[idx] = [val1, val2]
    elif kdx == None:
        number[idx][jdx] = [val1, val2]
    elif ldx == None:
        number[idx][jdx][kdx] = [val1, val2]
    else:
        number[idx][jdx][kdx][ldx] = [val1, val2]

def magnetude(number):
    numCopy = number[:]
    for idx, val in enumerate(numCopy):
        if isinstance(val, int):
            continue
        for jdx, val2 in enumerate(val):
            if isinstance(val2, int):
                continue
            for kdx, val3 in enumerate(val2):
                if isinstance(val3, list):
                    numCopy[idx][jdx][kdx] = val3[0]*3 + val3[1]*2
    for idx, val in enumerate(numCopy):
        if isinstance(val, int):
            continue
        for jdx, val2 in enumerate(val):
            if isinstance(val2, list):
                numCopy[idx][jdx] = val2[0]*3 + val2[1]*2
    for idx, val in enumerate(numCopy):
        if isinstance(val, list):
            numCopy[idx] = val[0]*3 + val[1]*2
    numCopy = numCopy[0]*3 + numCopy[1]*2
    return numCopy


def reduce(number):
    action = True
    while action:
        action = False
        for idx, val in enumerate(number):
            if action:
                break
            if isinstance(val, int):
                continue
            for jdx, val2 in enumerate(val):
                if action:
                    break
                if isinstance(val2, int):
                    continue
                for kdx, val3 in enumerate(val2):
                    if action:
                        break
                    if isinstance(val3, int):
                        continue
                    for ldx, val4 in enumerate(val3):
                        if isinstance(val4, int):
                            continue
                        explode(number, idx, jdx, kdx, ldx)
                        action = True
                        break
        if not action:
            for idx, val in enumerate(number):
                if action:
                    break
                if isinstance(val, int):
                    if val >= 10:
                        split(number, idx, None, None, None)
                        action = True
                        break
                    continue
                for jdx, val2 in enumerate(val):
                    if action:
                        break
                    if isinstance(val2, int):
                        if val2 >= 10:
                            split(number, idx, jdx, None, None)
                            action = True
                            break
                        continue
                    for kdx, val3 in enumerate(val2):
                        if action:
                            break
                        if isinstance(val3, int):
                            if val3 >= 10:
                                split(number, idx, jdx, kdx, None)
                                action = True
                                break
                            continue
                        for ldx, val4 in enumerate(val3):
                            if isinstance(val4, int):
                                if val4 >= 10:
                                    split(number, idx, jdx, kdx, ldx)
                                    action = True
                                    break
                            continue
def part1():
    global numbers


    currNum = numbers[0]

    for n in numbers[1:]:
        currNum = [currNum, n]
        reduce(currNum)
        #print(currNum)
    print(magnetude(currNum))

def part2():
    global numbers
    
    localNumbers = numbers[:]
            
    maxi = 0

    for n1 in numbers:
        for n2 in numbers:
            if n1 == n2:
                continue
            n1Copy = copy.deepcopy(n1)
            n2Copy = copy.deepcopy(n2)
            currNum = [n1Copy, n2Copy]
            reduce(currNum)
            currSum = magnetude(currNum)
            if currSum > maxi:
                maxi = currSum
    print(maxi)
    

def main():
    #part1()
    part2()


if __name__ == "__main__":
    main()

    