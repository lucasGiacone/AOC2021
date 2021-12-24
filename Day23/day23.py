from dataclasses import dataclass
from typing import Optional
from copy import deepcopy as dp

if True:
    Filename = "Day23/input.txt"
elif True:
    Filename = "Day23/sample.txt"
else:
    Filename = "Day23/sample2.txt"


@dataclass
class casa:
    primeiro: Optional[str]
    segundo: Optional[str]

@dataclass
class novaCasa:
    primeiro: Optional[str]
    segundo: Optional[str]
    terceiro: Optional[str]
    quarto: Optional[str]


mapCasa = {
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3,
    0 : "A",
    1 : "B",
    2 : "C",
    3 : "D"
}

corredor = [None]*11
casaA = [None]*2
casaB = [None]*2
casaC = [None]*2
casaD = [None]*2


with open(Filename) as f:
    line = f.readline().strip()
    line = f.readline().strip()
    line = line.replace("#", "")
    corredor = [c if c != "." else None for c in line]
    for i in range(2):
        line = f.readline().strip().replace("#", "")
        casaA[i] = line[0] if line[0] != "." else None
        casaB[i] = line[1] if line[1] != "." else None
        casaC[i] = line[2] if line[2] != "." else None
        casaD[i] = line[3] if line[3] != "." else None
    casaA = casa(*casaA)
    casaB = casa(*casaB)
    casaC = casa(*casaC)
    casaD = casa(*casaD)
casas = [casaA, casaB, casaC, casaD]


invalidPosCorredor = {2,4,6,8}

distCasas = {
    "A" : {"B": 2, "C": 4, "D": 6},
    "B" : {"A": 2, "C": 2, "D": 4},
    "C" : {"A": 4, "B": 2, "D": 2},
    "D" : {"A": 6, "B": 4, "C": 2}
}

posCasaCorredor = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8,
    0 : 2,
    1 : 4,
    2 : 6,
    3 : 8
}

multipliers = {
    "A" : 1,
    "B" : 10,
    "C" : 100,
    "D" : 1000
}

@dataclass
class move:
    origin: str
    destiny: str
    distance: int


scores = set({})


def validMoves(corredor, casas):
    moves = []
    for idx, casa in enumerate(casas):
        if casa.primeiro is not None:
            multiplier = multipliers[casa.primeiro]
            if mapCasa[casa.primeiro] == idx:
                if mapCasa[casa.segundo] == idx:
                    continue
            for i in range(posCasaCorredor[idx], -1, -1):
                if corredor[i] is not None:
                    break
                elif i not in invalidPosCorredor:
                    moves.append(move(mapCasa[idx]+"1", i, (posCasaCorredor[idx] + 1 - i)*multiplier))
            for i in range(posCasaCorredor[idx]+1, len(corredor)):
                if corredor[i] is not None:
                    break
                elif i not in invalidPosCorredor:
                    moves.append(move(mapCasa[idx]+"1", i, (i - posCasaCorredor[idx] + 1)*multiplier))  
        elif casa.segundo is not None:
            multiplier = multipliers[casa.segundo]
            if mapCasa[casa.segundo] == idx:
                continue
            for i in range(posCasaCorredor[idx], -1, -1):
                if corredor[i] is not None:
                    break
                elif i not in invalidPosCorredor:
                    moves.append(move(mapCasa[idx]+"2", i, (posCasaCorredor[idx] + 2 - i) * multiplier))
            for i in range(posCasaCorredor[idx]+1, len(corredor)):
                if corredor[i] is not None:
                    break
                elif i not in invalidPosCorredor:
                    moves.append(move(mapCasa[idx]+"2", i, (i - posCasaCorredor[idx] + 2) * multiplier))
    for idx, pos in enumerate(corredor):
        if pos is not None:
            multiplier = multipliers[pos]
            casa = casas[mapCasa[pos]]
            validMove = True
            dist = 0
            if idx < posCasaCorredor[pos]:
                for j in range(idx+1, posCasaCorredor[pos]+1):
                    if corredor[j] is not None:
                        validMove = False
                        break
                dist = posCasaCorredor[pos] - idx
            else:
                for j in range(posCasaCorredor[pos], idx):
                    if corredor[j] is not None:
                        validMove = False
                        break
                dist = idx - posCasaCorredor[pos]
            if validMove and casa.primeiro is None:
                if casa.segundo is None:
                    moves.append(move(idx, pos+"2", (dist +2) * multiplier))
                elif casa.segundo == pos:
                    moves.append(move(idx, pos+"1", (dist +1) * multiplier))
                
    return moves
        

def win(casas):
    for idx, casa in enumerate(casas):
        if casa.primeiro != casa.segundo or casa.primeiro != mapCasa[idx]:
            return False
    return True


def printGame(corredor, casas):
    print("#############")
    print("#", end="")
    for el in corredor:
        if el:
            print(el, end="")
        else:
            print(".", end="")
    print("#")
    print("##", end = "")
    for casa in casas:
        if casa.primeiro:
            print(f"#{casa.primeiro}", end="")
        else:
            print("#.", end="")
    print("###")
    print("  ", end="")
    for casa in casas:
        if casa.segundo:
            print(f"#{casa.segundo}", end="")
        else:
            print("#.", end="")
    print("#")
    print("  #########")
    print()
    

minScore = float("inf")
def recursiveGame(corredor, casas, score, moveTrace):
    global minScore
    if win(casas):
        if score < minScore:
            minScore = score
            print(score)
            printGame(corredor, casas)
            print(moveTrace)
        return

    # printGame(corredor, casas)
    moves = validMoves(corredor, casas)
    # if moves:
    #     print(moves[0])
    # else:
    #     print("No moves")
    if len(moveTrace) <= 2:
            print(moveTrace)

    for move in moves:
        if score >= minScore:
            return
        newCorredor = dp(corredor)
        newCasas = dp(casas)
        if isinstance(move.origin, int):
            el, newCorredor[move.origin] = newCorredor[move.origin], None
            casa = newCasas[mapCasa[move.destiny[0]]]
            if move.destiny[1] == "1":
                casa.primeiro = el
            else:
                casa.segundo = el
            newCasas[mapCasa[move.destiny[0]]] = casa
        elif isinstance(move.destiny, int):
            casa = newCasas[mapCasa[move.origin[0]]]
            if move.origin[1] == "1":
                el, casa.primeiro = casa.primeiro, None
            else:
                el, casa.segundo = casa.segundo, None
            newCorredor[move.destiny] = el
            newCasas[mapCasa[move.origin[0]]] = casa
        else:
            casaOrigem = newCasas[mapCasa[move.origin[0]]]
            if move.origin[1] == "1":
                el, casaOrigem.primeiro = casaOrigem.primeiro, None
            else:
                el, casaOrigem.segundo = casaOrigem.segundo, None
            newCasas[mapCasa[move.origin[0]]] = casaOrigem
            casaDestino = newCasas[mapCasa[move.destiny[0]]]
            if move.destiny[1] == "1":
                casaDestino.primeiro = el
            else:
                casaDestino.segundo = el
            newCasas[mapCasa[move.destiny[0]]] = casaDestino
        moveTrace.append(move)
        recursiveGame(newCorredor, newCasas, score + move.distance, moveTrace)
        moveTrace.pop()
    return


def part1():
    global corredor, casas, minScore

    recursiveGame(corredor, casas, 0, [])
    print(minScore)


def novoWin(casas):
    for idx, casa in enumerate(casas):
        if not (casa.primeiro == casa.segundo == casa.terceiro == casa.quarto == mapCasa[idx]):
            return False
    return True


def novoValidMoves(corredor, casas):
    moves = []
    for idx, casa in enumerate(casas):
        if casa.primeiro is not None:
            multiplier = multipliers[casa.primeiro]
            if mapCasa[casa.primeiro] == mapCasa[casa.segundo] == mapCasa[casa.terceiro] == mapCasa[casa.quarto] == idx:
                continue
            for i in range(posCasaCorredor[idx], -1, -1):
                if corredor[i] is not None:
                    break
                elif i not in invalidPosCorredor:
                    moves.append(move(mapCasa[idx]+"1", i, (posCasaCorredor[idx] + 1 - i)*multiplier))
            for i in range(posCasaCorredor[idx]+1, len(corredor)):
                if corredor[i] is not None:
                    break
                elif i not in invalidPosCorredor:
                    moves.append(move(mapCasa[idx]+"1", i, (i - posCasaCorredor[idx] + 1)*multiplier))  
        elif casa.segundo is not None:
            multiplier = multipliers[casa.segundo]
            if mapCasa[casa.segundo] == mapCasa[casa.terceiro] == mapCasa[casa.quarto] == idx:
                continue
            for i in range(posCasaCorredor[idx], -1, -1):
                if corredor[i] is not None:
                    break
                elif i not in invalidPosCorredor:
                    moves.append(move(mapCasa[idx]+"2", i, (posCasaCorredor[idx] + 2 - i) * multiplier))
            for i in range(posCasaCorredor[idx]+1, len(corredor)):
                if corredor[i] is not None:
                    break
                elif i not in invalidPosCorredor:
                    moves.append(move(mapCasa[idx]+"2", i, (i - posCasaCorredor[idx] + 2) * multiplier))
        elif casa.terceiro is not None:
            multiplier = multipliers[casa.terceiro]
            if mapCasa[casa.terceiro] == mapCasa[casa.quarto] == idx:
                continue
            for i in range(posCasaCorredor[idx], -1, -1):
                if corredor[i] is not None:
                    break
                elif i not in invalidPosCorredor:
                    moves.append(move(mapCasa[idx]+"3", i, (posCasaCorredor[idx] + 3 - i) * multiplier))
            for i in range(posCasaCorredor[idx]+1, len(corredor)):
                if corredor[i] is not None:
                    break
                elif i not in invalidPosCorredor:
                    moves.append(move(mapCasa[idx]+"3", i, (i - posCasaCorredor[idx] + 3) * multiplier))
        elif casa.quarto is not None:
            multiplier = multipliers[casa.quarto]
            if mapCasa[casa.quarto] == idx:
                continue
            for i in range(posCasaCorredor[idx], -1, -1):
                if corredor[i] is not None:
                    break
                elif i not in invalidPosCorredor:
                    moves.append(move(mapCasa[idx]+"4", i, (posCasaCorredor[idx] + 4 - i) * multiplier))
            for i in range(posCasaCorredor[idx]+1, len(corredor)):
                if corredor[i] is not None:
                    break
                elif i not in invalidPosCorredor:
                    moves.append(move(mapCasa[idx]+"4", i, (i - posCasaCorredor[idx] + 4) * multiplier))

    for idx, pos in enumerate(corredor):
        if pos == 'C' and idx == 5 and corredor[0] == 'A':
            pass
        if pos is not None:
            multiplier = multipliers[pos]
            casa = casas[mapCasa[pos]]
            dist = abs(posCasaCorredor[mapCasa[pos]] - idx)
            if casa.primeiro is None:
                if casa.segundo is None:
                    if casa.terceiro is None:
                        if casa.quarto is None and checkValidMove(corredor, idx, posCasaCorredor[pos]):
                            moves.append(move(idx, pos+"4", (dist +4) * multiplier))
                        elif casa.quarto == pos and checkValidMove(corredor, idx, posCasaCorredor[pos]):
                            moves.append(move(idx, pos+"3", (dist +3) * multiplier))
                    elif casa.terceiro == casa.quarto == pos and checkValidMove(corredor, idx, posCasaCorredor[pos]):
                        moves.append(move(idx, pos+"2", (dist +2) * multiplier))
                elif casa.segundo == casa.terceiro == casa.quarto == pos and checkValidMove(corredor, idx, posCasaCorredor[pos]):
                    moves.append(move(idx, pos+"1", (dist +1) * multiplier))
    return moves

def checkValidMove(corredor, origin, destiny):
    
    origin, destiny = (origin+1, destiny) if origin < destiny else (destiny+1, origin)

    for i in range(origin, destiny):
        if corredor[i] is not None:
            return False
    return True

def recursiveGame2(corredor, casas, score, moveTrace):
    global minScore
    if novoWin(casas):
        if score < minScore:
            minScore = score
            print(score)
            printGame(corredor, casas)
            print(moveTrace)
        return

    moves = novoValidMoves(corredor, casas)
    if len(moveTrace) <= 2:
            print(moveTrace)
    
    for move in moves:
        if score + move.distance >= minScore:
            continue
        newCorredor = dp(corredor)
        newCasas = dp(casas)
        if isinstance(move.origin, int):
            el, newCorredor[move.origin] = newCorredor[move.origin], None
            casa = newCasas[mapCasa[move.destiny[0]]]
            if move.destiny[1] == "1":
                casa.primeiro = el
            elif move.destiny[1] == "2":
                casa.segundo = el
            elif move.destiny[1] == "3":
                casa.terceiro = el
            else:
                casa.quarto = el
            newCasas[mapCasa[move.destiny[0]]] = casa
        elif isinstance(move.destiny, int):
            casa = newCasas[mapCasa[move.origin[0]]]
            if move.origin[1] == "1":
                el, casa.primeiro = casa.primeiro, None
            elif move.origin[1] == "2":
                el, casa.segundo = casa.segundo, None
            elif move.origin[1] == "3":
                el, casa.terceiro = casa.terceiro, None
            else:
                el, casa.quarto = casa.quarto, None
            newCorredor[move.destiny] = el
            newCasas[mapCasa[move.origin[0]]] = casa
        else:
            casaOrigem = newCasas[mapCasa[move.origin[0]]]
            if move.origin[1] == "1":
                el, casaOrigem.primeiro = casaOrigem.primeiro, None
            elif move.origin[1] == "2":
                el, casaOrigem.segundo = casaOrigem.segundo, None
            elif move.origin[1] == "3":
                el, casaOrigem.terceiro = casaOrigem.terceiro, None
            else:
                el, casaOrigem.quarto = casaOrigem.quarto, None
            newCasas[mapCasa[move.origin[0]]] = casaOrigem
            casaDestino = newCasas[mapCasa[move.destiny[0]]]
            if move.destiny[1] == "1":
                casaDestino.primeiro = el
            elif move.destiny[1] == "2":
                casaDestino.segundo = el
            elif move.destiny[1] == "3":
                casaDestino.terceiro = el
            else:
                casaDestino.quarto = el
            newCasas[mapCasa[move.destiny[0]]] = casaDestino
        moveTrace.append(move)
        recursiveGame2(newCorredor, newCasas, score + move.distance, moveTrace)
        moveTrace.pop()
    return


def part2():
    global corredor, casas, minScore
    novaFileira = [["D", "C", "B", "A"], ["D", "B", "A", "C"]]

    novasCasas = []
    for idx, casa in enumerate(casas):
        novasCasas.append(novaCasa(casa.primeiro, novaFileira[0][idx], novaFileira[1][idx] ,casa.segundo))

    recursiveGame2(corredor, novasCasas, 0, [])
    print(minScore)



def main():
    #part1()
    part2()
    pass

if __name__ == "__main__":
    main()