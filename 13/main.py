def check(one, two):
    l = min(len(one), len(two))
    for i in range(l):
        if one[::-1][i] != two[i]:
            return False
    return True

def find_ver(c, anti=None):
    t = [''.join([c[i][j] for i in range(len(c))]) for j in range(len(c[0]))]
    return find_hor(t, anti)

def find_hor(c,anti=None):
    for i in range(1,len(c)):
        if check(c[0:i], c[i:]) and i!=anti:
            return i 
    return None

d = [c.split() for c in open(0).read().split('\n\n')]

v = 0
h = 0
records = []
for i,c in enumerate(d):
    V=find_ver(c)
    H=find_hor(c)
    if V: 
        v += V 
        records.append((V,'V'))

    elif H: 
        h += H 
        records.append((H,'H'))
print(v+100*h)


def show(s):
    for l in s:
        print(l)
    print()

def smudge(c):
    for i in range(len(c)):
        for j in range(len(c[0])):
            C = [[t for t in l] for l in c]
            C[i][j] = "#" if c[i][j] == "." else "."
            yield [''.join(t) for t in C]

v = 0
h = 0
for i,c in enumerate(d):
    f = 0
    for s in smudge(c):
        V = find_ver(s,records[i][0] if records[i][1] == "V" else None)
        H = find_hor(s,records[i][0] if records[i][1] == "H" else None)
        if V: 
            v += V 
            f = 1
            break
        if H:
            h += H
            f = 1
            break
    if f == 0:
        show(c)
        break

print(v+100*h)

