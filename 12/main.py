import itertools

d = open(0).read().splitlines()

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

s = 0 
for line in d:
    record = line.split()[0]
    nums = [*map(int, line.split()[1].split(','))]
    n = find(record, nums)
    #print(record, nums, n)
    s += n

print(s)

# for line in d:
#     record = line.split()[0]
#     record = '.'.join([t for t in record.split('.') if t])
#     nums = [*map(int, line.split()[1].split(','))]
#     record = '?'.join(record for _ in range(5))
#     n = []
#     for i in range(5):
#         n.extend(nums)
#     nums = n  
#     #n = find(record, nums)
#     print(record, nums)
#     #s += n


