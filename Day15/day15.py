from __future__ import annotations
from dataclasses import dataclass
import math
import queue

if True:
    Filename = "Day15/input.txt"
else:
    Filename = "Day15/sample.txt"

@dataclass
class node:
    val : int
    visited : bool
    connections : list[node]
    distance : int = math.inf
    queueed: bool = False


def listInsert(node,lista):
    for i, n in enumerate(lista):
        if n.distance <= node.distance:
            lista.insert(i, node)
            return
    lista.insert(0,node)

        


def explore(node,lista):
    for n in node.connections:
        if not n.visited:
            n.distance = min(n.val + node.distance, n.distance)
            if not n.queueed:
                n.queueed = True
                if not lista:
                    lista.append(n)
                else:
                    listInsert(n, lista)
    node.visited = True
    



def part1():
    riskMap = []
    with open(Filename) as f:
        line = f.readline().strip()
        while line:
            riskMap.append([node(int(c), False, []) for c in line])
            line = f.readline().strip()

    head = riskMap[0][0]
    head.distance = 0
        
    for row, line in enumerate(riskMap):
        for col, n in enumerate(line):
            if col != 0:
                n.connections.append(riskMap[row][col-1])
            if row != 0:
                n.connections.append(riskMap[row-1][col])
            if row != len(riskMap)-1:
                n.connections.append(riskMap[row+1][col])
            if col != len(line)-1:
                n.connections.append(riskMap[row][col+1])

    lista = []
    explore(head, lista)
    
    while lista:
        explore(lista.pop(), lista)
    
    print(riskMap[-1][-1].distance)


def part2():
    newMap = []
    with open(Filename) as f:
        line = f.readline().strip()
        while line:
            lineStart = [node(int(c), False, []) for c in line]
            extension = []
            for i in range(1,5):
                extentedLine = []
                for n in lineStart:
                    val = n.val + i if n.val + i < 10 else n.val + i - 9
                    extentedLine.append(node(val, False, []))
                extension.extend(extentedLine)
            lineStart.extend(extension)
            line = f.readline().strip()
            newMap.append(lineStart)


    mapExtend = []
    for i in range (1,5):
        extension = []
        for line in newMap:
            extentedLine = []
            for n in line:
                val = n.val + i if n.val + i < 10 else n.val + i - 9
                extentedLine.append(node(val, False, []))
            extension.append(extentedLine)
        mapExtend.extend(extension)

    newMap.extend(mapExtend)



    head = newMap[0][0]
    head.distance = 0
        
    for row, line in enumerate(newMap):
        for col, n in enumerate(line):
            if col != 0:
                n.connections.append(newMap[row][col-1])
            if row != 0:
                n.connections.append(newMap[row-1][col])
            if row != len(newMap)-1:
                n.connections.append(newMap[row+1][col])
            if col != len(line)-1:
                n.connections.append(newMap[row][col+1])

    print("start")

    lista = []
    explore(head, lista)
    
    while lista:
        explore(lista.pop(), lista)
    
    print(newMap[-1][-1].distance)
    


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()