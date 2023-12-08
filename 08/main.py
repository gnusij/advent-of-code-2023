from math import lcm
d=open(0).read().splitlines()
I,G=[0 if c=='L' else 1 for c in d[0]],{k:n[1:-1].split(', ') for k,n in [l.split(' = ') for l in d[2:]]}
def f(p,c):
    i=1 
    while i:
        p=G[p][I[(i-1)%len(I)]]
        if c(p): 
            return i
        i+=1
print(f('AAA',lambda x:x=='ZZZ'),lcm(*[f(p,lambda x:x[2]=='Z') for p in [p for p in G if p[2]=='A']]))