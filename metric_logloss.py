#!/usr/bin/env python
import math

def metric(p_truth, p_pred):
    sum_entropy = 0
    pv = 0
    with open(p_pred) as fp:
      for line in open(p_truth):
        pv += 1
        label = int(line.strip().split(' ')[0])
        if label>1: label=1
        pred = float(fp.readline().strip().split(' ')[0])
        pred = max(1e-10, min(pred, 1-1e-10))
        logloss = label * math.log(pred) + (1-label) * math.log(1-pred) 
        sum_entropy += logloss
    
    logloss = -sum_entropy / pv
    print 'logloss= %.6f' % logloss 
    return logloss 

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print '<usage> %s groundtruth prediction' % sys.argv[0]
        exit(1)
    metric(sys.argv[1], sys.argv[2])

