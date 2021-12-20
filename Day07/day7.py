from __future__ import annotations
from dataclasses import dataclass
from functools import partial
from typing import cast
from math import sqrt

@dataclass
class data:
    states: dict[int, int]
    dp : list[int]
    maxVal : int

def parseInput():
    states = dict({})
    maxVal = 0
    with open('Day07\input.txt', 'r') as f:
        for state in f.readline().split(','):
            states[int(state)] = 1 if int(state) not in states else states[int(state)] + 1
            maxVal = max(maxVal, int(state))
    dp = [0] * (maxVal + 1)
    for i in states:
        dp[i] = states[i]
    for i in range(1, len(dp)):
        dp[i] += dp[i - 1]
    return data(states, dp, maxVal)

def part1(parsedInput) -> None:
    val = 0
    for i in parsedInput.states:
        val += parsedInput.states[i]*i
    oldVal = val
    i = 1
    total = parsedInput.dp[-1]
    while i < len(parsedInput.dp):
        val += (2*parsedInput.dp[i-1] - parsedInput.dp[-1])
        if val > oldVal:
            break
        oldVal = val
        i+=1
    print(oldVal)


def part2(parsedInput) -> None:
    val = 0
    steps = []
    multi = []
    for i in parsedInput.states:
        val += parsedInput.states[i]*i*(i+1)/2
        steps.append(-i)
        multi.append(parsedInput.states[i])

    for idx, step in enumerate(steps):
        steps[idx] = step if step != 0 else 1

    oldVal = val
    while True:
        for idx, val_i in enumerate(steps):
            val += val_i*multi[idx]
            #steps[idx] += 1
            steps[idx] = 1 if steps[idx] == -1 else steps[idx]+1
        if val > oldVal:
            break
        oldVal = val
    print(oldVal)

    # print(val)
    # oldVal = val
    # i = 1
    # total = parsedInput.dp[-1]
    # while i < len(parsedInput.dp):
    #     val += (2*parsedInput.dp[i-1] - parsedInput.dp[-1])
    #     if val > oldVal:
    #         break
    #     oldVal = val
    #     i+=1
    # print(oldVal)

def main():
    parsedInput = parseInput()
    # part1(parsedInput)
    part2(parsedInput)


if __name__ == "__main__":
    main()