#!/usr/bin/env python
import random

def metric(p_truth, p_pred):
    tot_truth, tot_false = 0, 0
    for line in open(p_truth):
        label = int(line.strip().split(' ')[0])
        if label>0: tot_truth += label
        else: tot_false += 1
    if tot_truth==0 or tot_false==0:
        print 'no truth or false'
        return 0

    pairs = []
    with open(p_pred) as fp:
      for line in open(p_truth):
        label = int(line.strip().split(' ')[0])
        pred = float(fp.readline().strip().split(' ')[0])
        pairs.append((label, pred))
    random.shuffle(pairs)
    sort_pairs = sorted(pairs, key=lambda d:-d[1])

    remain_false = tot_false 
    tot_score = 0.
    for label, pred in sort_pairs:
        if label > 0:
            tot_score += label * remain_false
        else:
            remain_false -= 1
    auc = tot_score / (tot_truth * tot_false)
    print 'AUC= %.6f' % auc 
    return auc

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print '<usage> %s groundtruth prediction' % sys.argv[0]
        exit(1)
    metric(sys.argv[1], sys.argv[2])

