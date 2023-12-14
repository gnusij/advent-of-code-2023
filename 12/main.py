import sys; sys.setrecursionlimit(1000000)
import itertools

d = open("example.txt").read().splitlines()

from math import comb

def replace(record, com):
    record = [t for t in record]
    indexes = [i for i,t in enumerate(record) if t == '?']
    for i,ind in enumerate(indexes):
        record[ind] = com[i]
    return ''.join(record)

def brute(record):
    records = []
    for com in list(itertools.product([".", "#"], repeat=record.count("?"))):
        records.append(replace(record, com))
    return records

def array_equal(ar1, ar2):
    for i in range(len(ar1)):
        if ar1[i] != ar2[i]:
            return False
    return True 

def validate(nums, pos):
    if pos.count('#') == sum(nums):
        cont = [t for t in pos.split('.') if t]
        if len(cont) == len(nums) and array_equal([len(t) for t in cont], nums):
                return True
    return False

def find(record, nums):
    c = 0
    for pos in brute(record):
        if validate(nums, pos):
            c += 1
    return c

# s = 0 
# for line in d:
#     record = line.split()[0]
#     nums = [*map(int, line.split()[1].split(','))]
#     n = find(record, nums)
#     print(record, nums, n)
#     s += n
# print(s)

for line in d:
    record = line.split()[0]
    nums = [*map(int, line.split()[1].split(','))]
    record = '?'.join(record for _ in range(5))
    record = '.'.join([t for t in record.split('.') if t])
    n = []
    for i in range(5):
        n.extend(nums)
    nums = n  
    #n = find(record, nums)
    #print(record, nums)
    #s += n



def study(record, num):

    # find all 
    pass


def drop(record, num):
    # first-last starts with #
    txt = [t for t in record] 

    if txt[0]==".": txt.pop(0)
    if txt[-1]==".": txt.pop(-1)

    if txt[0]=="#" and "." not in txt[0:num[0]]:
        txt = txt[num[0]+1:]
        num.pop(0)
        if num == []: return txt, num

    elif txt[-1]=="#" and "." not in txt[len(txt)-num[-1]:len(txt)]:
        txt = txt[:len(txt)-num[-1]-1]
        num.pop(-1)
        if num == []: return txt, num

    # first-last starts with ? but . in the way
    elif txt[0]=='?' and '.' in txt[0:num[0]]:
        txt = txt[''.join(txt).find('.')+1:]
        if num == []: return txt, num

    elif txt[-1]=='?' and '.' in txt[len(txt)-num[-1]:len(txt)]:
        txt = txt[:''.join(txt).rfind('.')-2]

    # first letter ?, next #, and num[0] = 1
    if txt[0]=='?' and num[0]==1:
        return [], []
        
    if txt[0]=='?' and txt[1]=='#' and num[0]==1:
        txt = txt[3:]
        num = num[1:] 
        if num == []: return txt, num
    
    if txt[0]=='?' and array_equal(txt[1:num[0]+1],'#'*num[0]):
        txt = txt[2+num[0]:]
        num = num[1:] 
        if num == []: return txt, num
        
    # only 1 possibility based on length 
    if len(txt) == sum(num)+len(num)-1:
        txt = []
        num = []
        if num == []: return txt, num

    # only 1 possibility based on num: e.g. ???. [1, 1, ...] 
    if "#." not in txt and len(txt) == sum(num)+1:
        txt = txt[sum(num)+1:]
        num = [] 
        if num == []: return txt, num

    # last portion can be removed
    tmp = ''.join(txt).split('.')[-1]
    if txt[::-1][0] == "?" and len(tmp) < num[-1] and "#" not in tmp:
        txt = txt[:len(txt)-len(tmp)]

    # there is .#####.  
    tmp = []
    for t in ''.join(txt).split('.'):
        if t == "#"*len(t) and len(t) in num:
            num.remove(len(t))
        else:
            tmp.append(t)
    txt = [t for t in '.'.join(tmp)]


    if txt == [] or num == []: return txt, num

    if txt[0]=="#" or txt[-1]=="#":
        txt, num = drop(txt, num)   

    #print(txt, num)
    return txt, num

C = 0

def valid(txt, num):
    #global C
    # find all possible orientiations for the first number
    C = 0
    def do(txt, num):
        nonlocal C
        #print(txt, num, c)
        if len(num) == 1:
            from math import comb
            C += comb(txt.count('?'), num[0])

        elif len(num) > 1:
            for i in range(len(txt)):
                if "." not in txt[i:i+num[0]] and len(txt)-i > (sum(num[1:]) + len(num[1:]) ):
                    newt = txt[:]
                    if i-1>0:
                        newt[i-1] = '.' 
                    newt[i:i+num[0]] = '#'*num[0]
                    if i+num[0]<len(txt):
                        newt[i+num[0]] = '.'
                    
                    newt[:i] = "."*i
                    do(txt[i+num[0]+1:], num[1:])

    do(txt, num)
    return C

def firstlast(line):
    record = line.split()[0]
    #record = '?'.join(record for _ in range(5))
    record = '.'.join([t for t in record.split('.') if t])
    num = [*map(int, line.split()[1].split(','))]
    #n = []
    #for i in range(5):
    #    n.extend(num)
    #num = n  

    #record = line.split()[0]
    #num = [*map(int, line.split()[1].split(','))]
    c = 1

    #print(record, num)
    txt, num = drop(record, num)
    #print(txt, num)

    v = valid(txt, num)
    v = v if v!=0 else 1
    print(record, v)

    #print(record, C)
    #n = find(''.join(txt), num)
    #print(n)
        
    #if array_equal([len(x) for x in ''.join([t for t in txt if t!='?']).split('.') if x], num):
    #    return c
    return v

c = 0
for i, l in enumerate(d):
    print(i+1)
    c+=firstlast(l)
print(c)

#t = '.???..?##?.??? 3,4'
#firstlast(t)
