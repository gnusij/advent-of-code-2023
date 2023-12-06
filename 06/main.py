d=[*map(lambda x:x.split(':')[1].split(),open(0).readlines())]
f=lambda T,D:str(sum([1 for t in range(int(T)+1) if t*(int(T)-t)>int(D)]))
print(eval('*'.join([f(*i) for i in zip(*d)])),f(*map(lambda x:int(''.join(x)),d)))