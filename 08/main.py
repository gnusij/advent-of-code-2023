
from collections import defaultdict

d = open(0).read().splitlines()

inst = d[0]
I = [0 if c == "L" else 1 for c in d[0]]
d = d[2:]

G = defaultdict(list)
Apos = []

for line in d:
    key, node = line.split(" = ")
    node = node.replace('(','').replace(')','')
    node = [n.strip() for n in node.split(',')]

    G[key].extend(node)
    if key.endswith("A"):
        Apos.append(key)

def p1(curpos='AAA'):
    endpos = 'ZZZ'
    i = 1 
    while True:
        curpos = G[curpos][I[(i-1)%len(I)]]
        if curpos == endpos:
            return i
        i += 1

def p2(curpos):
    i = 1 
    while True:
        curpos = G[curpos][I[(i-1)%len(I)]]
        if curpos.endswith("Z"):
            return i
        i+=1


def part2():
    print(Apos)

    i = 1
    while True:
        if inst[(i-1)%len(inst)] == "L":
            j = 0
        else:
            j = 1

        nextPos = [G[pos][j] for pos in Apos] 
        allz = 1
        for pos in nextPos:
            if not pos.endswith("Z"):
                allz = 0
        
        if allz:
            break
        else:
            Apos = nextPos
            i+=1
    print(i)


from math import lcm

print(p1())
print(lcm(p2('GNA'),p2('FCA'),p2('AAA'),p2('MXA'),p2('VVA'),p2('XHA')))