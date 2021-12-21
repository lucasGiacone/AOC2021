from copy import deepcopy as dp

table6mod10 = [0,6,2,8,4]

if True:
    Filename = "Day21/input.txt"
else:
    Filename = "Day21/sample.txt"

p1Pos = 0
p2Pos = 0
with open(Filename) as f:
    line = f.readline().strip()
    p1Pos = int(line.split(" ")[-1])
    line = f.readline().strip()
    p2Pos = int(line.split(" ")[-1])
print(p1Pos, p2Pos)


def part1():
    global p1Pos, p2Pos
    currP1pos = p1Pos
    currP2pos = p2Pos
    p1Score = 0
    p2Score = 0
    diceThrows = 0
    diceThrowsMod5 = 1
    while True:
        currP1pos = currP1pos + table6mod10[diceThrowsMod5]
        currP1pos = currP1pos if currP1pos <= 10 else currP1pos - 10
        p1Score += currP1pos
        diceThrows += 3
        
        if p1Score >= 1000:
            print("P1 won", p1Score)
            print("p2Score", p2Score)
            print("solution", diceThrows*p2Score)
            break
        currP2pos = currP2pos + table6mod10[diceThrowsMod5] + 9
        currP2pos = currP2pos if currP2pos <= 10 else currP2pos - 10
        currP2pos = currP2pos if currP2pos <= 10 else currP2pos - 10
        p2Score += currP2pos
        diceThrows += 3

        if p2Score >= 1000:
            print("P2 won", p2Score)
            print("p1Score", p1Score)
            print("solution", diceThrows*p1Score)
            break
        diceThrowsMod5 = diceThrowsMod5 + 3
        diceThrowsMod5 = diceThrowsMod5 if diceThrowsMod5 < 5 else diceThrowsMod5 - 5




dicerows = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}
p1Wins = 0
p2Wins = 0
def newNewPart2(p1PositionScore,p2PositionScore, row, player, multiplier):
    global p1Wins, p2Wins
    newP1PositionScore = {}
    newP2PositionScore = {}
    if player:
        for p1Pos, p1Score in p1PositionScore.items():
            newP1Pos = p1Pos + row
            newP1Pos = newP1Pos if newP1Pos <= 10 else newP1Pos - 10
            
            newScore = p1Score + newP1Pos
            newP1PositionScore[newP1Pos] = newScore
            if newScore >= 21:
                p1Wins += multiplier
                return
        
        
        newP2PositionScore = dp(p2PositionScore)
    else:
        for p2Pos, p2Score in p2PositionScore.items():
            newP2Pos = p2Pos + row
            newP2Pos = newP2Pos if newP2Pos <= 10 else newP2Pos - 10
            
            newScore = p2Score + newP2Pos
            newP2PositionScore[newP2Pos] = newScore
            if newScore >= 21:
                p2Wins += multiplier
                return
        newP1PositionScore = dp(p1PositionScore)
    
    for row, rowCount in dicerows.items():
        newNewPart2(newP1PositionScore,newP2PositionScore, row, not player, rowCount * multiplier)
    return


def part2():
    global p1Pos, p2Pos

    p1DimensionsScorePosition = {p1Pos:0}
    p2DimensionsScorePosition = {p2Pos:0}


    for row, rowCount in dicerows.items():
        newNewPart2(p1DimensionsScorePosition, p2DimensionsScorePosition, row, True, rowCount)
        print("row: ", row)
        print(p1Wins, p2Wins)


def main():
    part1()
    part2()
    pass

if __name__ == "__main__":
    main()