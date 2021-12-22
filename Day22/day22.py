from __future__ import annotations
from copy import deepcopy as dp
from dataclasses import dataclass
from typing import List

if True:
    Filename = "Day22/input.txt"
elif True:
    Filename = "Day22/sample.txt"
else:
    Filename = "Day22/sample2.txt"

@dataclass
class Cuboid:
    turnOn: bool
    x: int
    dx: int
    y: int
    dy: int
    z: int
    dz: int

    def vol(self):
        return abs(self.dx * self.dy * self.dz) if self.turnOn else - abs(self.dx * self.dy * self.dz)


    def intercect(self, other):
        xIntercect = (self.x <= other.x < self.x + self.dx) or (other.x <= self.x < other.x + other.dx)
        yIntercect = (self.y <= other.y < self.y + self.dy) or (other.y <= self.y < other.y + other.dy)
        zIntercect = (self.z <= other.z < self.z + self.dz) or (other.z <= self.z < other.z + other.dz)
        return xIntercect and yIntercect and zIntercect

    def intercectedCuboid(self, other):
        xIntercect = [other.x, min(other.dx, self.dx + self.x - other.x)] if self.x < other.x else [self.x, min(self.dx, other.x + other.dx- self.x)]
        yIntercect = [other.y, min(other.dy, self.dy + self.y - other.y)] if self.y < other.y else [self.y, min(self.dy, other.y + other.dy- self.y)]
        zIntercect = [other.z, min(other.dz, self.dz + self.z - other.z)] if self.z < other.z else [self.z, min(self.dz, other.z + other.dz- self.z)]
        
        return Cuboid(self.turnOn, xIntercect[0], xIntercect[1], yIntercect[0], yIntercect[1], zIntercect[0], zIntercect[1])

    def removeIntercections(self, other: Cuboid) -> List[Cuboid]:
        returnCuboids = []
        # Separate the x cuboid planes
        if (newDx := other.x - self.x) > 0:
            returnCuboids.append(Cuboid(self.turnOn, self.x, newDx, self.y, self.dy, self.z, self.dz))
        if (newDx := self.x + self.dx - other.x - other.dx) > 0:
            returnCuboids.append(Cuboid(self.turnOn, other.x + other.dx, newDx, self.y, self.dy, self.z, self.dz))
        if (newDy := other.y - self.y) > 0:
            returnCuboids.append(Cuboid(self.turnOn, other.x, other.dx, self.y, newDy, self.z, self.dz))
        if (newDy := self.y + self.dy - other.y - other.dy) > 0:
            returnCuboids.append(Cuboid(self.turnOn, other.x, other.dx, other.y + other.dy, newDy, self.z, self.dz))
        if (newDz := other.z - self.z) > 0:
            returnCuboids.append(Cuboid(self.turnOn, other.x, other.dx, other.y, other.dy, self.z, newDz))
        if (newDz := self.z + self.dz - other.z - other.dz) > 0:
            returnCuboids.append(Cuboid(self.turnOn, other.x, other.dx, other.y, other.dy, other.z + other.dz, newDz))
    
        return returnCuboids

cuboids = []

with open(Filename) as f:
    while line := f.readline().strip():
        state, coods = line.split(" ")
        x, y, z = map(lambda x: [int(i) for i in x[2:].split("..")], coods.split(","))
        cuboids.append(Cuboid(state == 'on', x[0], x[1] - x[0] + 1, y[0], y[1] - y[0] + 1, z[0], z[1] - z[0] + 1))


def validate(cuboid):
    if cuboid.x < -50 or cuboid.x + cuboid.dx > 51:
        return False
    if cuboid.y < -50 or cuboid.y + cuboid.dy > 51:
        return False
    if cuboid.z < -50 or cuboid.z + cuboid.dz > 51:
        return False
    return True


def part1():
    resultCuboids = []
    validCuboids = [cuboid for cuboid in cuboids if validate(cuboid)]
    for newCuboid in validCuboids:
        totalVol = 0
        intersectedCuboids = []
        
        for oldCuboid in resultCuboids:
            if newCuboid.intercect(oldCuboid):
                intersectedCuboids.append(oldCuboid)
    
        if newCuboid.turnOn:
            if not intersectedCuboids:
                resultCuboids.append(newCuboid)
            else:
                newCuboidParts = [newCuboid]
                noIntersectionParts = []
                while newCuboidParts:
                    part = newCuboidParts.pop()
                    intersectionCube = None
                    for intersectedCuboid in intersectedCuboids:
                        if part.intercect(intersectedCuboid):
                            intersectionCube = intersectedCuboid
                            break
                    else:
                        noIntersectionParts.append(part)
                        continue
                    intersection = part.intercectedCuboid(intersectionCube)
                    newCuboidParts.extend(part.removeIntercections(intersection))
                resultCuboids.extend(noIntersectionParts)
        elif not newCuboid.turnOn:
            if intersectedCuboids:
                for intersectedCuboid in intersectedCuboids[:]:
                    intersection = newCuboid.intercectedCuboid(intersectedCuboid)
                    addedCuboids = intersectedCuboid.removeIntercections(intersection)
                    idx = resultCuboids.index(intersectedCuboid)
                    resultCuboids.pop(idx)
                    resultCuboids.extend(addedCuboids)
                

    for r in resultCuboids:
        totalVol += r.vol()
    print(totalVol)
    return


def dumbPart1():
    points = {}
    for i in range(0, 101):
        points[i-50] = {}
        for j in range(0, 101):
            points[i-50][j-50] = {}
            for k in range(0, 101):
                points[i-50][j-50][k-50] = False
    vol = 0
    for cuboid in cuboids:
        for i in range(cuboid.x, cuboid.x + cuboid.dx):
            for j in range(cuboid.y, cuboid.y + cuboid.dy):
                for k in range(cuboid.z, cuboid.z + cuboid.dz):
                    if points[i][j][k]:
                        if not cuboid.turnOn:
                            points[i][j][k] = False
                            vol -= 1
                    elif cuboid.turnOn:
                        points[i][j][k] = True
                        vol += 1
        print(vol)
        


def part2():
    resultCuboids = []
    for newCuboid in cuboids:
        totalVol = 0
        intersectedCuboids = []
        
        for oldCuboid in resultCuboids:
            if newCuboid.intercect(oldCuboid):
                intersectedCuboids.append(oldCuboid)
    
        if newCuboid.turnOn:
            if not intersectedCuboids:
                resultCuboids.append(newCuboid)
            else:
                newCuboidParts = [newCuboid]
                noIntersectionParts = []
                while newCuboidParts:
                    part = newCuboidParts.pop()
                    intersectionCube = None
                    for intersectedCuboid in intersectedCuboids:
                        if part.intercect(intersectedCuboid):
                            intersectionCube = intersectedCuboid
                            break
                    else:
                        noIntersectionParts.append(part)
                        continue
                    intersection = part.intercectedCuboid(intersectionCube)
                    newCuboidParts.extend(part.removeIntercections(intersection))
                resultCuboids.extend(noIntersectionParts)
        elif not newCuboid.turnOn:
            if intersectedCuboids:
                for intersectedCuboid in intersectedCuboids[:]:
                    intersection = newCuboid.intercectedCuboid(intersectedCuboid)
                    addedCuboids = intersectedCuboid.removeIntercections(intersection)
                    idx = resultCuboids.index(intersectedCuboid)
                    resultCuboids.pop(idx)
                    resultCuboids.extend(addedCuboids)
                

    for r in resultCuboids:
        totalVol += r.vol()
    print(totalVol)
    return


def main():
    part1()
    # print("\n\n\n")
    # dumbPart1()
    part2()
    pass

if __name__ == "__main__":
    main()