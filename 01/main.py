d = open(0).read().split()
def f(d, N):
    s = 0 
    for l in d:
        S = ''
        for i in range(len(l)):
            if l[i].isnumeric():
                S += l[i]
            for j,n in enumerate(N):
                if l[i:].startswith(n):
                    S += str(j+1)
        s += int(S[0] + S[-1])
    print(s) 
f(d,[])
f(d,['one','two','three','four','five','six','seven','eight','nine'])