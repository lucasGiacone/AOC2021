from dataclasses import dataclass

if True:
    Filename = "Day13/input.txt"
else:
    Filename = "Day13/sample.txt"

@dataclass
class point:
    x: int
    y: int


points = []
instructions = []
with open(Filename) as f:
    line = f.readline().strip()
    while line:
        points.append(point(*[int(c) for c in line.split(",")]))
        line = f.readline().strip()

    line = f.readline().strip()
    while line:
        line = line.split(" ")[2].split("=")
        if line[0] == "x":
            instructions.append(point(int(line[1]), -1))
        else:
            instructions.append(point(-1, int(line[1])))
        line = f.readline().strip()




def foldY(y):
    for p in points[:]:
        np = point(p.x, p.y)
        if np.y > y:
            points.remove(p)
            np.y = y - (np.y - y)
            if np not in points:
                points.append(np)
    

def foldX(x):
    for p in points[:]:
        np = point(p.x, p.y)
        if np.x > x:
            np.x = x - (np.x - x)
            points.remove(p)
            if np not in points:
                points.append(np)

def printPoints():
    xMax = 0
    yMax = 0
    for p in points:
        if p.x > xMax:
            xMax = p.x
        if p.y > yMax:
            yMax = p.y
    dPoints = [["." for x in range(xMax+1)] for y in range(yMax+1)]
    for p in points:
        dPoints[p.y][p.x] = "#"
    for y in range(yMax+1):
        for x in range(xMax+1):
            print(dPoints[y][x], end="")
        print()


def part1():
    for i in instructions:
        if i.x == -1:
            foldY(i.y)
        else:
            foldX(i.x)
        break
    print(len(points))
    pass

def part2():
    for i in instructions:
        if i.x == -1:
            foldY(i.y)
        else:
            foldX(i.x)
    printPoints()
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()