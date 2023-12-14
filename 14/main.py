d = [[t for t in l] for l in open(0).read().split()]

def T(d):
    return [[d[i][j] for i in range(len(d))] for j in range(len(d[0]))]

def M(d,t=0,m=1):
    changed=0
    if t:d = T(d)                   # W E
    if m!=1: R=range(1,len(d))[::-1] # N W
    else: R=range(len(d)-1)          # S E
    for i in R:
        for j in range(len(d[0])):
            if d[i][j] == "O" and d[i+m][j] not in "#O":
                d[i+m][j] = "O"
                d[i][j] = "."
                changed=1
    if t:d = T(d)
    if changed:
        return M(d,t,m)
    else:
        return d

def load(d):
    l = 0
    for i in range(len(d)):
        for j in range(len(d[0])):
            if d[::-1][i][j] == "O":
                l += i+1 
    return l

print(load(M(d,0,-1)))

seen = [''.join([''.join(l) for l in d])] 
i = 1
while True:
    d = M(M(M(M(d,0,-1),1,-1),0,1),1,1)
    txt = ''.join([''.join(l) for l in d])
    if txt in seen:
        start = seen.index(txt)
        repeat = i-seen.index(txt)
        break
    else:
        seen.append(txt)
    i += 1
d = [seen[start+(1000000000-start)%repeat][i:i+len(d[0])] for i in range(0, len(seen[0]), len(d[0]))]
print(load(d))