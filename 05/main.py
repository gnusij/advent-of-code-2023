d = open(0).read().split('\n\n')
def t(v,m):
    for d, s, r in m:
        if s <= v < s + r:
            return d + (v - s)
    return v
def r(n,F):
    r = n
    for f in F:
        r = f(r)
    return r
S = [*map(int,d[0].split(":")[1].split())]
M = [[[*map(int,i.split())] for i in l.split(":\n")[1].split('\n')] for l in d[1:]]
F = [lambda v,i=i: t(v,M[i]) for i in range(7)]

def T(v,m):
    for d, s, r in m:
        if d <= v < d + r:
            return s + (v - d)
    return v
def c(n):
    for x, y in zip(S[::2], S[1::2]):
        if x <= n < x + y:
            return 1
    return 0

n = 0
F = [lambda v,i=i: T(v,M[i]) for i in range(7)[::-1]]
while 1:
    if c(r(n, F)):
        break
    n+=1

print(min(r(n,F) for n in S), n)
