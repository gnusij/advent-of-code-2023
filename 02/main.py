d = open(0).read().splitlines()
s,S=0,0
for i, l in enumerate(d):
    o,R,G,B=1,1,1,1
    for y in l.split(":")[1].split(";"):
        for e in [x.strip() for x in y.split(",")]:
            n, t = e.split()
            n=int(n)
            if (t=="red" and n>12) or (t=="green" and n>13) or (t=="blue" and n>14):
                o = 0
            if t=="red":R=max(R,n)
            if t=="green":G=max(G,n)
            if t=="blue":B=max(B,n)
    if o:s += i+1
    S += R*G*B
print(s,S)
