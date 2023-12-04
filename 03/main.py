import re
from collections import defaultdict
D = open(0).read().split()
d = [[t for t in d] for d in D]
N = '0123456789'
G = defaultdict(list)

def c(y,x1,x2,n):
    def g(j,i):
        try: return d[j][i] 
        except: return '.'
    for j in range(y-1,y+2):
        for i in range(x1-1,x2+1):
            if j>=0 and i>=0:
                if g(j ,i) == '*':
                    G[(j,i)].append(n)
                if g(j, i) not in N+'.': 
                    return True
    return False

s = 0
for j,line in enumerate(D):
    for m in re.finditer(r'\d+', line):
        n = int(m.group(0))
        if c(j, m.start(), m.end(), n):
            s += n

S = 0
for k,v in G.items():
    if len(v) == 2:
        S += v[0] * v[1]
print(s, S)