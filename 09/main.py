
#d = [[int(x) for x in l] for l in open(0).read().splitlines()]


d= [[*map(int, l.split())] for l in open(0).read().splitlines()]


def findinc(l):
    newlist = []
    for i in range(1, len(l)):
        newlist.append(l[i]-l[i-1])
    return newlist


s = 0
S = 0
for line in d:

    newlist = line
    seq = [line]
    
    while any(newlist):
        newlist = findinc(newlist)
        seq.append(newlist)

    newval = sum([l[-1] for l in seq])

    #print(seq)
    tmps = 0
    for i in range(len(seq))[::-1]:
        #print(i, seq[i-1][0], tmps)
        tmps = seq[i-1][0] - tmps
    S += tmps*-1
    print(seq, tmps)
    #print(seq)

    s += newval
print(s,S)