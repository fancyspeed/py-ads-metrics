#!/usr/bin/env python
import math

def metric(p_truth, p_pred):
    pv, sum_click = 0, 0
    for line in open(p_truth):
        label = int(line.strip().split(' ')[0])
        if label>1: label=1
        sum_click += label
        pv += 1.
    average_ctr = sum_click / pv
    average_entropy = average_ctr * math.log(average_ctr) + (1-average_ctr) * math.log(1-average_ctr)

    sum_entropy = 0
    with open(p_pred) as fp:
      for line in open(p_truth):
        label = int(line.strip().split(' ')[0])
        if label>1: label=1
        pred = float(fp.readline().strip().split(' ')[0])
        pred = max(1e-10, min(pred, 1-1e-10))
        logloss = label * math.log(pred) + (1-label) * math.log(1-pred) 
        sum_entropy += logloss
    
    ne = sum_entropy / pv / average_entropy
    #print -sum_entropy / pv, -average_entropy
    print 'NE= %.6f' %  ne 
    return ne 

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print '<usage> %s groundtruth prediction' % sys.argv[0]
        exit(1)
    metric(sys.argv[1], sys.argv[2])

