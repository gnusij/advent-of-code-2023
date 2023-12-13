def reflect(x, y):
    for i in range(min(len(x), len(y))):
        if x[::-1][i] != y[i]:
            return 0
    return 1

def find(c, anti=0, t=0):
    if t==1:
        c = [[c[i][j] for i in range(len(c))] for j in range(len(c[0]))]
        return find(c, anti, t=0)
    for i in range(1,len(c)):
        if reflect(c[0:i], c[i:]) and i!=anti:
            return i 
    return 0

def smudge(c):
    for i in range(len(c)):
        for j in range(len(c[0])):
            C = [[t for t in l] for l in c]
            C[i][j] = "#" if c[i][j] == "." else "."
            yield C 

d = [c.split() for c in open(0).read().split('\n\n')]
s,S,R = 0,0,[]

for i,c in enumerate(d):
        
    for j in [1,100]:
        if v:=find(c,t=j): 
            s += v*j
            R.append((v,j))
    
    for C in smudge(c):
        b = 0
        for j in [1,100]:
            if v:=find(C,R[i][0] if R[i][1]==j else 0,j):
                S += v*j 
                b = 1
        if b: break
print(s,S)