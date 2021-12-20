from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto


class wires(Enum):
    a = auto()
    b = auto()
    c = auto()
    d = auto()
    e = auto()
    f = auto()
    g = auto()

numDisplay = {
    0 : [wires.a, wires.b, wires.c, wires.e, wires.f, wires.g],
    1 : [wires.c, wires.f],
    2 : [wires.a, wires.c, wires.d, wires.e, wires.g],
    3 : [wires.a, wires.c, wires.d, wires.f, wires.g],
    4 : [wires.b, wires.c, wires.d, wires.f],
    5 : [wires.a, wires.b, wires.d, wires.f, wires.g],
    6 : [wires.a, wires.b, wires.d, wires.e, wires.f, wires.g],
    7 : [wires.a, wires.c, wires.f],
    8 : [wires.a, wires.b, wires.c, wires.d, wires.e, wires.f, wires.g],
    9 : [wires.a, wires.b, wires.c, wires.d, wires.f, wires.g],
}


# wireMap = {
#     "a" : [wires.a, wires.b, wires.c, wires.d, wires.e, wires.f, wires.g],
#     "b" : [wires.a, wires.b, wires.c, wires.d, wires.e, wires.f, wires.g],
#     "c" : [wires.a, wires.b, wires.c, wires.d, wires.e, wires.f, wires.g],
#     "d" : [wires.a, wires.b, wires.c, wires.d, wires.e, wires.f, wires.g],
#     "e" : [wires.a, wires.b, wires.c, wires.d, wires.e, wires.f, wires.g],
#     "f" : [wires.a, wires.b, wires.c, wires.d, wires.e, wires.f, wires.g],
#     "g" : [wires.a, wires.b, wires.c, wires.d, wires.e, wires.f, wires.g],
# }

@dataclass
class input:
    before: list[str]
    after: list[str]


def parseInput():
    with open("Day08\input.txt", "r") as f:
        for line in f:
            before, after = line.split(" | ")
            before = before.split()
            after = after.split()
            yield input(before, after)

def part1() -> None:
    parsedInput = parseInput()
    inputQuant = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    for line in parsedInput:
        currLine = line.after
        for wires in currLine:
            match len(wires):
                case 2: # 2 wires
                    inputQuant[1] += 1
                case 3:
                    inputQuant[7] += 1
                case 4:
                    inputQuant[4] += 1
                case 7:
                    inputQuant[8] += 1
                case _:
                    pass
        
    print(inputQuant[1] + inputQuant[4] + inputQuant[7] + inputQuant[8])
    return


def part2() -> None:
    parsedInput = parseInput()
    numSum = 0
    for line in parsedInput:
        currLine = line.before
        numberWireMap = {
            6: [], 0: [], 9: [],
            2: [], 3: [], 5: [],
        }
        wireMap = {}
        for numWires in currLine:
            numWires = sorted(numWires)
            numWires = "".join(numWires)
            match len(numWires):
                case 2: # 2 wires
                    numberWireMap[1] = numWires
                case 3:
                    numberWireMap[7] = numWires
                case 4:
                    numberWireMap[4] = numWires
                case 7:
                    numberWireMap[8] = numWires
                case 6:
                    numberWireMap[0].append(numWires)
                    numberWireMap[6].append(numWires)
                    numberWireMap[9].append(numWires)
                case 5:
                    numberWireMap[2].append(numWires)
                    numberWireMap[3].append(numWires)
                    numberWireMap[5].append(numWires)
                case _:
                    print("Error")
                    exit()

        for letter in numberWireMap[7]:
            if letter not in numberWireMap[1]:
                wireMap[wires.a] = letter
                break

        for poss in numberWireMap[9]:
            inside = True
            for letter in numberWireMap[4]:
                if letter not in poss:
                    inside = False
                    break
            if inside:
                numberWireMap[9] = poss
                break

        
        for letter in numberWireMap[8]:
            if letter not in numberWireMap[9]:
                wireMap[wires.e] = letter
                break


        newSix = []
        newFive = []
        for poss in numberWireMap[6]:
            if wireMap[wires.e] in poss:
                newSix.append(poss)

        for poss in numberWireMap[5]:
            if wireMap[wires.e] not in poss:
                newFive.append(poss)


        for poss in newFive:
            poss1 = sorted(poss+wireMap[wires.e])
            poss1 = "".join(poss1)
            for poss2 in newSix:
                if poss1 == poss2:
                    numberWireMap[5] = poss
                    numberWireMap[6] = poss2
                    break

        for poss in numberWireMap[0]:
            for letter in numberWireMap[8]:
                if letter not in poss:
                    if letter not in numberWireMap[1] and letter in numberWireMap[4]:
                        wireMap[wires.d] = letter
                        numberWireMap[0] = poss
        

        for letter in numberWireMap[4]:
            if letter not in numberWireMap[1] and letter != wireMap[wires.d]:
                wireMap[wires.b] = letter
                break

        for poss in numberWireMap[3]:
            letterNotIn3 = []
            for letter in numberWireMap[8]:
                if letter not in poss:
                    letterNotIn3.append(letter)
            if wireMap[wires.b] in letterNotIn3 and wireMap[wires.e] in letterNotIn3:
                numberWireMap[3] = poss
                break

        for letter in numberWireMap[4]:
            if letter not in numberWireMap[5]:
                wireMap[wires.c] = letter
                break
        
        for letter in numberWireMap[1]:
            if letter != wireMap[wires.c]:
                wireMap[wires.f] = letter
                break

        for poss in numberWireMap[2]:
            if wireMap[wires.b] not in poss and wireMap[wires.f] not in poss:
                numberWireMap[2] = poss
                break

        #print(numberWireMap)

        for key in numberWireMap:
            numberWireMap[key] = "".join(sorted(numberWireMap[key]))

        wireNumberMap = {v: str(k) for k, v in numberWireMap.items()}

        nums = line.after
        for idx, num in enumerate(nums):
            nums[idx] = "".join(sorted(num))

        result = ""
        try:
            for num in nums:
                result += wireNumberMap[num]
            numSum += int(result)
        except:
            print("Error --------------------------------------------------")
            print(result)
            print(wireNumberMap)
            print(num)
            print("Error --------------------------------------------------")

    print(numSum)
    return
    

def main():
    # part1()
    part2()


if __name__ == "__main__":
    main()