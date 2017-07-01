#!/usr/bin/env python
import math

def metric(p_truth, p_pred):
    sum_error = 0
    pv = 0
    with open(p_pred) as fp:
      for line in open(p_truth):
        pv += 1
        label = int(line.strip().split(' ')[0])
        if label>1: label=1
        pred = float(fp.readline().strip().split(' ')[0])
        loss = (label - pred) ** 2
        sum_error += loss
    
    rmse = math.sqrt( sum_error / pv )
    print 'RMSE= %.6f' %rmse 
    return rmse 

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print '<usage> %s groundtruth prediction' % sys.argv[0]
        exit(1)
    metric(sys.argv[1], sys.argv[2])

