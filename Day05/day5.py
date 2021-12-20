from __future__ import annotations
from dataclasses import dataclass
from typing import cast

@dataclass
class data:
    coords: list[tuple[coord, coord]]

@dataclass
class coord:
    x : int
    y : int


def parseInput():
    coords = []
    with open('Day05\input.txt', 'r') as f:
        for line in f:
            c0, c1 = line.split(" -> ")
            c0 = coord(*[int(i) for i in c0.strip().split(",")])
            c1 = coord(*[int(i) for i in c1.strip().split(",")])
            coords.append((c0, c1))
    return data(coords)


def sign(num: int) -> int:
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

def drawLine(table, line):
    dx = sign(line[1].x - line[0].x)
    dy = sign(line[1].y - line[0].y)
    it = dx*(line[1].x - line[0].x) if dx != 0 else dy*(line[1].y - line[0].y)
    # try:
    for i in range(it+1):
        table[line[0].y + dy*i][line[0].x + dx*i] += 1
    # except:
    #     print(line[0].y + dy*i)
    #     print(line[0].x + dx*i)

def dumpTable(table):
    for line in table:
        for i in line:
            char = i if i != 0 else "."
            print(char, end=" ")
        print()


def part1(parsedInput) -> None:
    size = 1000
    table = [[0 for i in range(size)] for j in range(size)]
    #dumpTable(table)
    intersections = 0
    for line in parsedInput.coords:
        if line[0].x == line[1].x or line[0].y == line[1].y:
            drawLine(table, line)
    #dumpTable(table)
    for line in table:
        for elem in line:
            if elem > 1:
                intersections += 1
    print(f"Part 1: {intersections}")
    return

def part2(parsedInput) -> None:
    size = 1000
    table = [[0 for i in range(size)] for j in range(size)]
    #dumpTable(table)
    intersections = 0
    for line in parsedInput.coords:
        drawLine(table, line)
    #dumpTable(table)
    for line in table:
        for elem in line:
            if elem > 1:
                intersections += 1
    print(f"Part 2: {intersections}")
    return

def main():
    parsedInput = parseInput()
    part1(parsedInput)
    part2(parsedInput)


if __name__ == "__main__":
    main()