from math import ceil
from dataclasses import dataclass

if True:
    Filename = "Day16/input.txt"
else:
    Filename = "Day16/sample.txt"

binStr = ""

hexToBin = { "0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111" }

with open(Filename) as f:
    line = f.readline().strip()
    for c in line:
        binStr += hexToBin[c]

print(binStr)

@dataclass
class packet:
    version: int
    id: str
    data: int = 0

versions = []
packets = []

def analyze_packet(binStr):
    global versions
    global packets
    packetVersion = binStr[:3]
    versions.append(int(packetVersion,2))
    packetId = binStr[3:6]
    #print(binStr)
    #print(f"Packet version: {packetVersion} - {int(packetVersion, 2)}\npacket id: {packetId}")=
    if packetId == "100": #valor literal
        packetLen = 0
        valBinStr = ""
        while binStr[6+packetLen*5] != '0':
            valBinStr += binStr[7+packetLen*5:11+packetLen*5]
            packetLen+=1
        valBinStr += binStr[7+packetLen*5:11+packetLen*5]
        val = int(valBinStr,2)
        packetLen+=1
        packetSize = packetLen*5 + 6
        packets.append(packet(int(packetVersion,2), int(packetId,2), val))
        return binStr[packetSize:]
    else:
        if binStr[6] == '1':
            lengthId = 11
            numberOfSubPackets = int(binStr[7:lengthId+7], 2)
            packets.append(packet(int(packetVersion,2), int(packetId,2), numberOfSubPackets))
            currBinStr = binStr[lengthId+7:]
            for _ in range(numberOfSubPackets):
                currBinStr = analyze_packet(currBinStr)
            return currBinStr
        else :
            lengthId = 15
            subPacketSize = int(binStr[7:lengthId+7],2)
            P = packet(int(packetVersion,2), int(packetId,2), subPacketSize)
            packets.append(P)
            currBinStr = binStr[lengthId+7:lengthId+7+subPacketSize]
            numberOfSubPackets = 0
            while len(currBinStr) > 6:
                numberOfSubPackets += 1
                currBinStr = analyze_packet(currBinStr)
            idx = packets.index(P)
            if numberOfSubPackets == 0:
                exit(1)
            packets[idx].data = numberOfSubPackets
            return binStr[subPacketSize+7+15:]


def newAnalizePacket(binStr):
    packetVersion = binStr[:3]
    packetId = binStr[3:6]
    if packetId == "100": #valor literal
        packetLen = 0
        valBinStr = 0
        while binStr[6+packetLen*5] != '0':
            valBinStr += binStr[7+packetLen*5:11+packetLen*5]
            packetLen+=1
        valBinStr += binStr[7+packetLen*5:11+packetLen*5]
        val = int(valBinStr,2)
        packetLen+=1
        packetSize = packetLen*5 + 6
        return binStr[packetSize:]


def part1():
    global binStr, versions
    localBinStr = binStr[:]
    analyze_packet(localBinStr)
    print(sum(versions))

def evaluate(packets):
    global cnt
    packet = packets.pop(0)
    if packet.id == 4:
        return packet.data
    elif packet.id == 0:
        sumList = []
        for _ in range(packet.data):
            sumList.append(evaluate(packets))
        return sum(sumList)
    elif packet.id == 1:
        prodList = []
        for _ in range(packet.data):
            prodList.append(evaluate(packets))
        res = 1
        for i in prodList:
            res *= i
        return res
    elif packet.id == 2:
        minList = []
        for _ in range(packet.data):
            minList.append(evaluate(packets))
        return min(minList)
    elif packet.id == 3:
        maxList = []
        for _ in range(packet.data):
            maxList.append(evaluate(packets))
        return max(maxList)
    elif packet.id == 5:
        return int(evaluate(packets) > evaluate(packets))
    elif packet.id == 6:
        return int(evaluate(packets) < evaluate(packets))
    elif packet.id == 7:
        return int(evaluate(packets) == evaluate(packets))


def part2():
    global binStr, versions, packets
    localBinStr = binStr[:]
    analyze_packet(localBinStr)
    print(evaluate(packets))

    

def main():
    part1()
    part2()


if __name__ == "__main__":
    main()