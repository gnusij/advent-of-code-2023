d = open(0).read().splitlines()
s,S,C=0,0,[1 for l in d]
for i,l in enumerate(d):
    W,N=map(lambda x:set(x.split()),l.split(":")[1].split('|'))
    m=len(N&W)
    for j in range(i+1,i+1+m):
        C[j]+=C[i]
    s+=int(2**(m-1))
    S+=C[i]
print(s,S)
