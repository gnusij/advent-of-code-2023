import sys; sys.setrecursionlimit(10000000)
from collections import defaultdict

G = defaultdict(list)
d = open(0).read().splitlines()

def get(J,I):
    if J>=0 and I>=0 and J<len(d) and I<len(d[0]):
        return d[J][I]
    return ''

def D():
    if get(j+1,i) in "|LJ":
        G[(j,i)].append((j+1,i))
def U():
    if get(j-1,i) in "|7F":
        G[(j,i)].append((j-1,i))
def R():
    if get(j,i+1) in "-7J":
        G[(j,i)].append((j,i+1))
def L():
    if get(j,i-1) in "-LF":
        G[(j,i)].append((j,i-1))

M = {
    '|':[U,D],
    '-':[L,R],
    'L':[U,R],
    'J':[U,L],
    '7':[D,L],
    'F':[D,R],
    'S':[U,D,L,R],
}

for j,l in enumerate(d):
    for i,t in enumerate(l):
        for f in M.get(t, []):
            f()

        if t=="S":
            startI = i
            startJ = j

def find_path(curr, visited):
    visited.append(curr)
    for node in G.get(curr, []):
        if node not in visited:
            find_path(node, visited)
    return visited

path = find_path((startJ,startI), [])
print(len(path)//2)

from matplotlib.path import Path
pltp = Path(path)
s=0
for j in range(len(d)):
    for i in range(len(d[0])):
        if pltp.contains_points([(j,i)]) and (j,i) not in path: 
            s +=1
print(s)