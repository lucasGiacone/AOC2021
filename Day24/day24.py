from alu import *
from multiprocessing import Process

if True:
    Filename = "Day24/input.txt"
elif True:
    Filename = "Day24/sample.txt"
else:
    Filename = "Day24/sample2.txt"

# with open(Filename) as f:
#     output = ""
#     output += "from __future__ import annotations\n"
#     output += "from functools import lru_cache\n\n"

#     funcCount = 0
#     while line := f.readline().strip():
#         op = line.split(" ")
#         if op[0] == "inp":
#             if funcCount:
#                 output += "\treturn z"
#                 output += "\n\n\n"
#             funcCount += 1
#             output += "@lru_cache(maxsize=None)\n"
#             output += f"def func{funcCount}(w: int, z: int) -> int:\n"
#         elif op[0] == "mul":
#             if op[2] == "0":
#                 output += f"\t{op[1]} = 0\n"
#             else:
#                 output += f"\t{op[1]} *= {op[2]}\n"
#         elif op[0] == "add":
#             output += f"\t{op[1]} += {op[2]}\n"
#         elif op[0] == "mod":
#             output += f"\t{op[1]} %= {op[2]}\n"
#         elif op[0] == "div":
#             output += f"\t{op[1]} //= {op[2]}\n"
#         elif op[0] == "eql":
#             output += f"\t{op[1]} = int({op[1]} == {op[2]})\n"
#     output += "\treturn z"
#     # with open("Day24/alu.py", "w+") as f:
#     #     f.write(output)


funcs = [func1, func2, func3, func4, func5, func6, func7, func8, func9, func10, func11, func12, func13, func14]
validIns = set()
validOuts = set()


results = []


def recursiveOut(zGoal = 0, depth = 0, currStack = [], minimun = None):
    if depth == 14:
        string = ""
        for c in currStack[::-1]:
            string += str(c)
        print(f"{string}")
    if depth >= 12:
        print(f"{depth} {currStack}")
    else:
        for w in range(1, 10):
            currStack.append(w)
            upperZ = 0
            minDelta = funcs[13-depth](w, upperZ) - zGoal
            while True:
                delta = funcs[13-depth](w, upperZ) - zGoal
                if not delta:
                    recursiveOut(upperZ, depth+1, currStack)
                    break
                elif minDelta + 500000 < delta:
                    break
                if delta < minDelta:
                    minDelta = delta
                upperZ += 1
            currStack.pop()
        return



deepInput9 = set()
input9Dict = {}

def part1():
    # Esse codigo não rodou até compleção mas acredito que ele conseguiria,
    # parei no meio pois obtive o valor maximo e um valor relativamente baixo para a segunda parte
    vals = []
    for w in range(1, 10):
        upperZ = 0
        while True:
            zUpper = funcs[13](w, upperZ)
            if not zUpper:
                vals.append(upperZ)   
                break
            upperZ += 1
    processes = []

    for idx, v in enumerate(vals):
        processes.append(Process(target=recursiveOut, args=(v, 1, [idx+1])))

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    # exit()




def part2():
    #Valor minimo obtido no inicio da busca da parte 1
    # 16181112741521
    # Por analize final 1521 se repetiu
    # Logo precisamos analizar apenas 1xxxxxxxxxxxxxx1521
    # 10**9 digitos, computacionalmente aceitavel


    j = 618111274 + 1
    count = 0
    while j > 0:
        if count % 10000000 == 0:
            print(j)
        count += 1
        j -= 1
        string = str(j)
        while "0" in string:
            idx = string[::-1].index("0")
            j -= 10**idx
            string = str(j)
        string = f"1{string}1521"
        if checkVal(string):
            exit()


def checkVal(w):
    z1  = funcs[ 0](int(w[0]), 0)
    z2  = funcs[ 1](int(w[1]), z1)
    z3  = funcs[ 2](int(w[2]), z2)
    z4  = funcs[ 3](int(w[3]), z3)
    z5  = funcs[ 4](int(w[4]), z4)
    z6  = funcs[ 5](int(w[5]), z5)
    z7  = funcs[ 6](int(w[6]), z6)
    z8  = funcs[ 7](int(w[7]), z7)
    z9  = funcs[ 8](int(w[8]), z8)
    z10 = funcs[ 9](int(w[9]), z9)
    z11 = funcs[10](int(w[10]), z10)
    z12 = funcs[11](int(w[11]), z11)
    z13 = funcs[12](int(w[12]), z12)
    z14 = funcs[13](int(w[13]), z13)
    if not z14:
        print(f"{w} {z14}")
        return True

def main():
    part1()
    part2()
    pass

if __name__ == "__main__":
    main()