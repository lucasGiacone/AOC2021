from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

if True:
    Filename = "Day19/input.txt"
else:
    Filename = "Day19/sample.txt"

@dataclass
class Scanner:
    index: int
    positions: set[Position]
    marked: bool = False

    def __hash__(self) -> int:
        return hash(self.index)

@dataclass
class Position:
    x: int
    y: int
    z: int

    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y, self.z + other.z)

    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

def rotate(position, amount):
    newPos = deepcopy(position)
    match amount//4:
        case 0:
            pass
        case 1:
            newPos.x, newPos.y = newPos.y, -newPos.x
        case 2:
            newPos.x, newPos.z = newPos.z, -newPos.x
        case 3:
            newPos.x, newPos.y = -newPos.x, -newPos.y
        case 4:
            newPos.x, newPos.y = -newPos.y, newPos.x
        case 5:
            newPos.x, newPos.z = -newPos.z, newPos.x

    for _ in range(amount%4):
        newPos.y, newPos.z = newPos.z, -newPos.y
    return newPos


scanners = {}
with open(Filename) as f:
    line = f.readline()
    line = f.readline().strip()
    idx = 0
    positions = set({})
    while line:
        line = line.strip()
        if not line:
            scanners[idx] = Scanner(idx, positions, idx == 0)
            idx += 1
            positions = set({})
            f.readline()
            line = f.readline().strip()
        positions.add(Position(*[int(coord) for coord in line.split(",")]))
        line = f.readline()
    scanners[idx] = Scanner(idx, positions)

coords = {Position(0,0,0)}

def part1():
    scanner0 = deepcopy(scanners[0])

    distanceMapScanner0 = {}
    for p in scanner0.positions:
        distanceMapScanner0[p] = set({})
        for p2 in scanner0.positions:
            if p is p2:
                continue                
            distanceMapScanner0[p].add((p.x-p2.x)**2 + (p.y-p2.y)**2 + (p.z-p2.z)**2)

    while notMarked := [scanners[idx] for idx in scanners if not scanners[idx].marked]:
        for scanner in notMarked:
            currDistanceMap = {}
            for p in scanner.positions:
                currDistanceMap[p] = set({})
                for p2 in scanner.positions:
                    if p is p2:
                        continue
                    currDistanceMap[p].add((p.x-p2.x)**2 + (p.y-p2.y)**2 + (p.z-p2.z)**2)

            samePositions = []
            for b1 in currDistanceMap:
                for b2 in distanceMapScanner0:
                    c = sum(el in distanceMapScanner0[b2] for el in currDistanceMap[b1])                            
                    if c >= 11:
                        samePositions.append([b1,b2])

            if samePositions:
                for i in range(24):
                    if (dist := samePositions[0][1] - rotate(samePositions[0][0],i)) == samePositions[1][1] - rotate(samePositions[1][0],i):
                        coords.add(dist)
                        for p in scanner.positions:
                            scanner0.positions.add(rotate(p, i)+dist)

                        for p in scanner0.positions:
                            if not distanceMapScanner0.get(p):
                                distanceMapScanner0[p] = set({})
                            for p2 in scanner0.positions:
                                if p is p2:
                                    continue
                                distanceMapScanner0[p].add((p.x-p2.x)**2 + (p.y-p2.y)**2 + (p.z-p2.z)**2)
                        scanner.marked = True
                        break
    print(len(scanner0.positions))

def part2():
    maxDist = 0
    for p in coords:
        for p2 in coords:
            dist = p.manhattan(p2)
            maxDist = max(maxDist, dist)
    print(maxDist)
    return

def main():
    part1()
    part2()
    pass

if __name__ == "__main__":
    main()