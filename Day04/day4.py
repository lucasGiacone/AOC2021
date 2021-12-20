from dataclasses import dataclass

@dataclass
class data:
    board : list[list[int]]
    numbers : list[int]

def parseInput():
    with open('Day04\input.txt', 'r') as f:
        calledNumbers = [int(i) for i in f.readline().split(',')]
        boards = []
        while f.readline():
            board = []
            for _ in range(5):
                board.extend([int(num.strip()) for num in f.readline().split()])
            boards.append(board)
        return data(boards, calledNumbers)

def bingoCheck(board):
    for i in range(5):
        win = True
        for j in range(5):
            if board[i*5 + j] != -1:
                win = False
        if win:
            return True
    for j in range(5):
        win = True
        for i in range(5):
            if board[i*5 + j] != -1:
                win = False
        if win:
            return True
    return False





def part1(parsedInput) -> None:
    for number in parsedInput.numbers:
        for board in parsedInput.board:
            if number in board:
                board[board.index(number)] = -1
            if bingoCheck(board):
                #print(board)
                sum = 0
                for num in board:
                    if num != -1:
                        sum += num
                print(sum)
                print(number)
                print(sum*number)
                return


def printBoard(board):
    for i in range(5):
        print(board[i*5 : i*5 + 5])

def part2(parsedInput) -> None:
    currBoards = parsedInput.board[:]
    lastBoard = 0
    for number in parsedInput.numbers:
        for board in currBoards:
            if number in board:
                board[board.index(number)] = -1
                if bingoCheck(board):
                    # printBoard(board)
                    # print(number)
                    parsedInput.board.remove(board)
                    lastBoard = board[:]
        currBoards = parsedInput.board[:]
        if not len(currBoards):
            break
    printBoard(lastBoard)
    sum = 0
    for num in lastBoard:
        if num != -1:
            sum += num
    print(sum)
    print(number)
    print(sum*number)



def main():
    parsedInput = parseInput()
    # print(bingoCheck([-1, 2, 3, 4, 5, -1, 7, 8, 9, 10, -1, 12, 13, 14, 15, -1, 17, 18, 19, 20 , -1, 22, 23, 24, -1]))
    #part1(parsedInput)
    part2(parsedInput)


if __name__ == "__main__":
    main()