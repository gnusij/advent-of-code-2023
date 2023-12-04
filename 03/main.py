import re
from collections import defaultdict
d=open(0).read().split()
s,S,G=0,0,defaultdict(list)
def c(y,x,X,n):
    for j in range(y-1,y+2):
        for i in range(x-1,X+1):
            if j>=0 and i>=0 and j<len(d) and i<len(d[1]):
                v=d[j][i]
                if v=='*':G[(j,i)].append(n)
                if v not in '012345679.': 
                    return 1
    return 0
for j,l in enumerate(d):
    for m in re.finditer(r'\d+', l):
        n=int(m.group(0))
        if c(j,m.start(),m.end(),n):
            s+=n
for k,v in G.items():
    if len(v)==2:
        S+=v[0]*v[1]
print(s,S)