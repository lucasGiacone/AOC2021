from dataclasses import dataclass

@dataclass
class data:
    nLines : int
    lines : list[str]
    size : int

def parseInput():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        return data(len(lines), [line.strip() for line in lines], len(lines[0].strip()))

def part1(parsedInput) -> None:
    ones = [0 for _ in range(parsedInput.size)]
    for idx in range(parsedInput.size):
        for line in parsedInput.lines:
            if line[idx] == '1':
                ones[idx] += 1

    print(ones)
    x = 0
    for i in ones:
        x = x << 1
        if i > parsedInput.nLines / 2:
            x += 1
        
    print(x)
    print(x*((1<<parsedInput.size) - x -1))


def part2(parsedInput) -> None:
    ones = [0 for _ in range(parsedInput.size)]
    for idx in range(parsedInput.size):
        for line in parsedInput.lines:
            if line[idx] == '1':
                ones[idx] += 1


    epsilon = []
    gamma = []
    bitCriteria = ones[0] > parsedInput.nLines / 2
    for line in parsedInput.lines:
        if (line[0] == '1') == bitCriteria:
            epsilon.append(line)
        else:
            gamma.append(line)

    # print(epsilon)

    # print(len(gamma))
    idx = 1
    while len(epsilon) > 1:
        nOnes = 0
        nZeros = 0
        for line in epsilon:
            if line[idx] == '1':
                nOnes += 1
            else:
                nZeros += 1
        print(nOnes, nZeros)
        if nOnes >= nZeros:
            epsilon = [line for line in epsilon if line[idx] == '1']
        else:
            epsilon = [line for line in epsilon if line[idx] == '0']
        idx += 1
    print(epsilon)

    idx = 1
    while len(gamma) > 1:
        nOnes = 0
        nZeros = 0
        for line in gamma:
            if line[idx] == '1':
                nOnes += 1
            else:
                nZeros += 1
        print(nOnes, nZeros)
        if nOnes >= nZeros:
            gamma = [line for line in gamma if line[idx] == '0']
        else:
            gamma = [line for line in gamma if line[idx] == '1']
        idx += 1
    print(gamma)

    print(f"part 2:{int(epsilon[0],2) * int(gamma[0],2)}")



def main():
    parsedInput = parseInput()
    #part1(parsedInput)
    part2(parsedInput)


if __name__ == "__main__":
    main()