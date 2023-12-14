d = [[t for t in l] for l in open(0).read().split()]

def t(d):
    return [[d[i][j] for i in range(len(d))] for j in range(len(d[0]))]

def N(d):
    changed=0
    for i in range(1,len(d))[::-1]:
        for j in range(len(d[0])):
            if d[i][j] == "O" and d[i-1][j] not in "#O":
                d[i-1][j] = "O"
                d[i][j] = "."
                changed=1
    if changed:
        return N(d)
    else:
        return d

def W(d):
    d = t(d)
    changed=0
    for i in range(1,len(d))[::-1]:
        for j in range(len(d[0])):
            if d[i][j] == "O" and d[i-1][j] not in "#O":
                d[i-1][j] = "O"
                d[i][j] = "."
                changed=1
    if changed:
        return W(t(d))
    else:
        return t(d)

def S(d):
    changed=0
    for i in range(len(d)-1):
        for j in range(len(d[0])):
            if d[i][j] == "O" and d[i+1][j] not in "#O":
                d[i+1][j] = "O"
                d[i][j] = "."
                changed=1
    if changed:
        return S(d)
    else:
        return d

def E(d):
    d = t(d)
    changed=0
    for i in range(len(d)-1):
        for j in range(len(d[0])):
            if d[i][j] == "O" and d[i+1][j] not in "#O":
                d[i+1][j] = "O"
                d[i][j] = "."
                changed=1
    if changed:
        return E(t(d))
    else:
        return t(d)

def load(d):
    load = 0
    for i in range(len(d)):
        for j in range(len(d[0])):
            if d[::-1][i][j] == "O":
                load += i+1 
    return load

print(load(N(d)))

def cycle(d):
    d = N(d)
    d = W(d)
    d = S(d)
    d = E(d)
    return d

seen = [] 
orig = ''.join([''.join(l) for l in d])
seen.append(orig)

i = 1
while True:
    d = cycle(d)
    txt = ''.join([''.join(l) for l in d])

    if txt in seen:
        start = seen.index(txt)
        repeat = i-seen.index(txt)
        break
    else:
        seen.append(txt)
    i += 1

for i in range((1000000000-start)%repeat):
    d = cycle(d)

print(load(d))