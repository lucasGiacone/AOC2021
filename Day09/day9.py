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


if False:
    matrix = []
    sizex = 10
    sizey = 5
    with open('Day09\sample.txt', 'r') as f:
        for line in f:
            matrix.append(list(line.strip()))
else:
    matrix = []
    sizex = 100
    sizey = 100
    with open('Day09\input.txt', 'r') as f:
        for line in f:
            matrix.append(list(line.strip()))

def scanUp(x, y):
    if matrix[y][x] < matrix[y-1][x]:
        return True
    else:
        return False

def scanDown(x, y):
    if matrix[y][x] < matrix[y+1][x]:
        return True
    else:
        return False

def scanLeft(x, y):
    if matrix[y][x] < matrix[y][x-1]:
        return True
    else:
        return False

def scanRight(x, y):
    if matrix[y][x] < matrix[y][x+1]:
        return True
    else:
        return False

def scan(x,y):
    if y != 0:
        if not scanUp(x,y):
            return False
    if y != sizey-1:
        if not scanDown(x,y):
            return False
    if x != 0:
        if not scanLeft(x,y):
            return False
    if x != sizex-1:
        if not scanRight(x,y):
            return False
    return True

def part1():
        values = []
        for y in range(sizey):
            for x in range(sizex):
                if scan(x,y):
                    values.append(matrix[y][x])
        print(f'{values = }')
        print(f"{ sum([int(x) + 1 for x in values]) }")
                

searchStack = []
currSize = 0
def search(x,y):
    if x != 0:
        if matrix[y][x-1] != '9' and matrix[y][x-1] != -1:
            matrix[y][x-1] = -1
            searchStack.append((x-1,y))
    if x != sizex-1:
        if matrix[y][x+1] != '9' and matrix[y][x+1] != -1:
            print(f'{matrix[y][x+1] = }')
            matrix[y][x+1] = -1
            searchStack.append((x+1,y))
    if y != 0:
        if matrix[y-1][x] != '9' and matrix[y-1][x] != -1:
            matrix[y-1][x] = -1
            searchStack.append((x,y-1))
    if y != sizey-1:
        if matrix[y+1][x] != '9' and matrix[y+1][x] != -1:
            matrix[y+1][x] = -1
            searchStack.append((x,y+1))



def part2():
    global currSize
    sizes = []
    for y in range(sizey):
        for x in range(sizex):
            while searchStack:
                x_,y_ = searchStack.pop()
                search(x_,y_)
                currSize += 1
                pass

            if currSize > 0:
                sizes.append(currSize)
                currSize = 0
    
            match matrix[y][x]:
                case -1:
                    currSize = 0
                    pass
                case 9:
                    currSize = 0
                    pass
                case _:
                    search(x,y)
                    pass
    sizes.sort(reverse=True)
    print(f'{sizes = }')
    print(f'{sizes[0]*sizes[1]*sizes[2] = }')
    pass


def main():
    #part1()
    part2()


if __name__ == "__main__":
    main()