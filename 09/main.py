d=[[*map(int, l.split())] for l in open(0).read().split('\n')]
s,S=0,0
for n in d:
    Q=[n]
    while any(n:=[n[i]-n[i-1] for i in range(1,len(n))]):
        Q+=[n]
    s+=sum([q[-1] for q in Q])
    t=0
    for i in range(len(Q))[::-1]:
        t=Q[i][0]-t
    S+=t
print(s,S)