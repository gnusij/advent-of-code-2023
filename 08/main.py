from math import*
I,_,*G=open(0).read().splitlines()
I,G=[0 if c=='L' else 1 for c in I],{k:n[1:-1].split(', ') for k,n in [l.split(' = ') for l in G]}
def f(p,c,i=1):
    while~-c(p:=G[p][I[(i-1)%len(I)]]):i+=1
    return i
print(f('AAA',lambda x:x=='ZZZ'),lcm(*[f(p,lambda x:x[2]=='Z') for p in G if p[2]=='A']))