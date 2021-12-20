def part1():
    with open("input.txt") as f:
        lines = f.readlines()
        contador = 0
        old = int(lines[0])
        for line in lines:
            new = int(line)
            if new > old:
                contador += 1
            old = new
        print(contador)


def part2():
    with open("input.txt") as f:
        lines = f.readlines()
        contador = 0
        old = int(lines[0]) + int(lines[1]) + int(lines[2])
        for i in range(len(lines)-2):
            new = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
            if new > old:
                contador += 1
            old = new
        print(contador)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
