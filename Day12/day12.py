if True:
    Filename = "Day12/input.txt"
else:
    Filename = "Day12/sample2.txt"


class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.Upper = name[0] < "a"
    
    def add_connection(self, node):
        self.connections.append(node)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Node:{self.name}>"


start = Node("start")
end = Node("end")
nodes = {start.name: start, end.name: end}

with open(Filename) as f:
    for line in f:
        line = line.strip()
        before, after = line.split("-")
        if before not in nodes:
            before = Node(before)
            nodes[before.name] = before
        else:
            before = nodes[before]
        if after not in nodes:
            after = Node(after)
            nodes[after.name] = after
        else:
            after = nodes[after]
        before.add_connection(after)
        after.add_connection(before)


#print(nodes)

paths = 0
def explore(node, visited):
    global paths
    if node.name == "end":
        paths += 1
        return

    if not node.Upper:
        new_visited = visited.copy()
        new_visited.append(node)
    else:
        new_visited = visited.copy()

    for n in node.connections:
        if n not in visited:
            explore(n, new_visited)
    return

def part1():
    global paths, nodes
    paths = 0
    start = nodes["start"]
    explore(start, [])
    print(f"Part 1: {paths}")

    

def explore2(node, visited, smallcave = False):
    global paths
    if node.name == "end":
        paths += 1
        return

    if not node.Upper:
        new_visited = visited.copy()
        new_visited.append(node)
    else:
        new_visited = visited.copy()

    for n in node.connections:
        cnt = new_visited.count(n)
        if smallcave and cnt == 0:
            explore2(n, new_visited, smallcave)
        elif not smallcave and cnt < 2:
            explore2(n, new_visited, cnt == 1 )

    return

def part2():
    global paths, nodes
    paths = 0
    start = nodes["start"]
    explore2(start, [start])
    print(f"Part 2: {paths}")


def main():
    #part1()
    part2()


if __name__ == "__main__":
    main()