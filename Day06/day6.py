from __future__ import annotations
from dataclasses import dataclass

@dataclass
class data:
    states: list[int]

def parseInput():
    states = [0 for i in range(9)]
    with open('Day06\input.txt', 'r') as f:
        for state in f.readline().split(','):
            states[int(state)] += 1
    return data(states)


def part1(parsedInput) -> None:
    days = 80
    oldState = parsedInput.states
    currState = oldState
    for _ in range(days):
        currState = oldState[1:]
        currState.append(oldState[0])
        currState[6] += oldState[0]
        oldState = currState[:]
    print(f"part1 = {sum(currState)}")
    return

def part2(parsedInput) -> None:
    days = 256
    oldState = parsedInput.states
    currState = oldState
    for _ in range(days):
        currState = oldState[1:]
        currState.append(oldState[0])
        currState[6] += oldState[0]
        oldState = currState[:]
    print(f"part1 = {sum(currState)}")
    return

def main():
    parsedInput = parseInput()
    part1(parsedInput)
    part2(parsedInput)


if __name__ == "__main__":
    main()