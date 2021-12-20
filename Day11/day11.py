if True:
    Filename = "Day11/input.txt"
else:
    Filename = "Day11/sample.txt"

days = 100

table = []
with open(Filename) as f:
    for line in f:
        table.append([int(c) for c in line.strip()])
#print(table)

size_x = len(table[0])
size_y = len(table)


def tablePrint():
    for y in range(size_y):
        for x in range(size_x):
            print(table[y][x], end=" ")
        print()


flashes = 0
def part1():
    global flashes
    for _ in range(days):
        for y in range(size_y):
            for x in range(size_x):
                table[y][x] += 1
                if table[y][x] > 9:
                    flashes += 1
                    explodingQueue.append((x,y))
                    table[y][x] = -1
        while explodingQueue:
            explode(*explodingQueue.pop(0))
        for y in range(size_y):
            for x in range(size_x):
                if table[y][x] == -1:
                    table[y][x] = 0
    tablePrint()
    print("Flashes:", flashes)

possibleSteps = {
    (0,1),
    (1,0),
    (0,-1),
    (-1,0),
    (1,1),
    (1,-1),
    (-1,1),
    (-1,-1)
}

explodingQueue = []
def explode(x,y):
    global flashes
    for dx,dy in possibleSteps:
        if 0 <= x+dx < size_x and 0 <= y+dy < size_y and table[y+dy][x+dx] != -1:
            table[y+dy][x+dx] += 1
            if table[y+dy][x+dx] > 9:
                flashes += 1
                explodingQueue.append((x+dx,y+dy))
                table[y+dy][x+dx] = -1

def part2():
    days = 0
    while True:
        for y in range(size_y):
            for x in range(size_x):
                table[y][x] += 1
                if table[y][x] > 9:
                    explodingQueue.append((x,y))
                    table[y][x] = -1
        while explodingQueue:
            explode(*explodingQueue.pop(0))
        for y in range(size_y):
            for x in range(size_x):
                if table[y][x] == -1:
                    table[y][x] = 0
        days += 1
        for y in range(size_y):
            for x in range(size_x):
                if table[y][x] != 0:
                    break
            else:
                continue
            break
        else:
            print(days)
            break


def main():
    # part1()
    part2()


if __name__ == "__main__":
    main()