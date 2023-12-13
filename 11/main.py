d=open(0).read().splitlines()
r=range
e=enumerate
Y=r(len(d))
X=r(len(d[0]))
for P in [1, 1000000-1]:
    G = [(j,i) for j in Y for i in X if d[j][i]=='#']
    for m,E in e([[i for i in X if '#' not in [d[j][i] for j in Y]],[j for j in Y if '#' not in d[j]]]):
        for i,n in e(E):
            for j,k in e(G):
                y,x=k;G[j]=(y,x)
                if y>=n+(P*i) and m:G[j]=(y+P,x)
                elif x>=n+(P*i) and~-m:G[j]=(y,x+P)
    print(sum([abs(n1[1]-n2[1])+abs(n1[0]-n2[0]) for i,n1 in e(G) for j in r(i,len(G),1) if n1!=(n2:=G[j])]))