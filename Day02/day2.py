from dataclasses import dataclass

@dataclass
class data:
    direction: str
    distance: int

def parseInput():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        return [data(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]

def part1(parsedInput) -> None:
    x = 0
    y = 0
    for i in parsedInput:
        match (i.direction):
            case "forward":
                x += i.distance
            case "down":
                y += i.distance
            case "up":
                y -= i.distance
            case _:
                raise Exception("Invalid direction")
    print(f"part 1: {abs(x)*abs(y)}")

def part2(parsedInput) -> None:
    x = 0
    y = 0
    aim = 0
    for i in parsedInput:
        match (i.direction):
            case "forward":
                x += i.distance
                y += aim*i.distance
            case "down":
                aim += i.distance
            case "up":
                aim -= i.distance
            case _:
                raise Exception("Invalid direction")
    print(f"part 2: {abs(x)*abs(y)}")

def main():
    parsedInput = parseInput()
    part1(parsedInput)
    part2(parsedInput)


if __name__ == "__main__":
    main()