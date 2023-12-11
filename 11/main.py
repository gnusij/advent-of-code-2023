from collections import defaultdict 

G = defaultdict(list)
d = [[t for t in l] for l in open(0).read().splitlines()]

nodes = []
dists = {}
ROWS = []
COLS = []

E = 1000000-1


for j in range(len(d)):
    if '#' not in d[j]:
        ROWS.append(j)
for i in range(len(d[0])):
    if '#' not in [d[j][i] for j in range(len(d))]:
        COLS.append(i)

print(ROWS, COLS)

c = 1
for j in range(len(d)):
    for i in range(len(d[0])):
        if d[j][i] == '#':
            G[c] = (j,i) 
            nodes.append((j,i))
            c +=1

def row_expand(G, row, i):
    newg = {}
    for key,value in G.items():
        y,x = value
        if y >= row+(E*i): 
            newg[key] = (y+E,x)
        else:
            newg[key] = (y,x) 
    return newg

def col_expand(G, col,i):
    newg = {}
    for key,value in G.items():
        y,x = value
        if x >= col+(E*i): 
            newg[key] = (y,x+E)
        else:
            newg[key] = (y,x) 
    return newg

for i,row in enumerate(ROWS):
    G = row_expand(G,row, i)
for i,col in enumerate(COLS):
    G = col_expand(G,col, i)

print(G)

def find_dist(p1,p2):
    x1 = G[p1][0]
    y1 = G[p1][1]
    x2 = G[p2][0]
    y2 = G[p2][1]
    return abs(y2-y1) + abs(x2-x1) 


for node1, point1 in G.items():
    for node2, point2 in G.items():
        if node1 != node2:
            if (node1,node2) not in dists and (node2,node1) not in dists:
                dists[(node1,node2)] = find_dist(node1, node2)

print(len(dists))
print(sum(dists.values()))
