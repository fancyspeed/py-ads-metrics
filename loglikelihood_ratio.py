import math

def entropy(arr):
    tot = sum(arr)
    if tot <= 0: return 0
    ret = sum([(x+0.0)*math.log((x+0.0)/tot) for x in arr if x>0])
    return -ret

def loglikehihood_ratio(k11, k12, k21, k22):
    ret = entropy([k11,k12,k21,k22])
    ret -= entropy([k11,k12]) + entropy([k21,k22]) 
    ret -= entropy([k11,k21]) + entropy([k12,k22])
    tot = sum([k11, k12, k21, k22])
    return 2*ret/tot if tot>0 else 0

def similarity(k11, k12, k21, k22):
    return 1 - 1./(1 + loglikehihood_ratio(k11, k12, k21, k22))

def test():
    for a, b, c, d in [(1, 2, 2, 4),
                       (1, 10, 10, 100),
                       (1, 100, 10, 1000),
                       (10, 1000, 1000, 1000000),
                       (10, 10000, 10000, 1000000),
                       (10, 10000, 10, 1000000),
                       (10, 10, 10, 1000000),
                       (10, 10, 10, 10),
                       ]:
        print a, b, c, d
        print loglikehihood_ratio(a, b-a, c-a, d-b-c+a), similarity(a, b-a, c-a, d-b-c+a)

test()
