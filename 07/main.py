from collections import Counter
d = open(0).read().splitlines()
def f(l):
    h,b=l.split()
    h=h.translate(''.maketrans('TJQKA',f'A{C}CDE'))
    return max((sorted(Counter(h.replace(c,'0')).values())[::-1],h) for c in '23456789ABCDE'),int(b)
for C in 'B0':
    print(sum(r*b for r,(_,b) in enumerate(sorted(map(f,d)),1)))