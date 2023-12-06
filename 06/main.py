from math import prod
T,D = map(lambda x:[*map(int,x.split(":")[1].split())], open(0).readlines())
f = lambda T,D:sum([1 if t * (T-t) > D else 0 for t in range(T+1)])
print(prod([f(T[i],D[i]) for i in range(len(T))]), f(*map(lambda x:int(''.join(map(str,x))), [T,D])))