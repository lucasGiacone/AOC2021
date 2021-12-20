# 2199943210 1 0
# 3987894921 3 7 4 1
# 9856789892 5 8 2
# 8767896789 6 6
# 9899965678 8 5

# 0 = up
# 1 = down
# 2 = left
# 3 = right

from typing import Match


if True:
    Filename = "Day10/input.txt"
else:
    Filename = "Day10/sample.txt"

def part1():
    illegals = {")": 0, "}": 0, "]": 0, ">": 0}
    illegalsVal = {")": 3, "}": 1197, "]": 57, ">": 25137}
    with open(Filename) as f:
        for line in f:
            stack = []
            line = line.strip()
            oposite = {")": "(", "}": "{", "]": "[", ">": "<", "(": ")", "{": "}", "[": "]", "<": ">"}

            for c in line:
                if c in "([{<":
                    stack.append(c)
                elif c in ")]}>":
                    cOp = oposite[c]
                    poped = stack.pop()
                    if poped != cOp:
                        #print(f"Expected {oposite[poped]} but got {c}")
                        illegals[c] += 1
                        stack = []
                        break
    sum = 0    
    for k, v in illegals.items():
        sum += illegalsVal[k] * v
    print(sum)
    pass



def part2():
    missingVal = {")": 1, "}": 3, "]": 2, ">": 4}
    scores = []
    with open(Filename) as f:
        for line in f:
            stack = []
            line = line.strip()
            oposite = {")": "(", "}": "{", "]": "[", ">": "<", "(": ")", "{": "}", "[": "]", "<": ">"}

            for c in line:
                if c in "([{<":
                    stack.append(c)
                elif c in ")]}>":
                    cOp = oposite[c]
                    poped = stack.pop()
                    if poped != cOp:
                        #print(f"Expected {oposite[poped]} but got {c}")
                        stack = []
                        break
            currScore = 0
            while stack:
                c = stack.pop()
                currScore *= 5
                currScore += missingVal[oposite[c]]
            if currScore:
                scores.append(currScore)
            scores.sort()
    print(scores[(len(scores)-1)//2])
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()