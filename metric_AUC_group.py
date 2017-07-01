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

    pred_dict = {}
    with open(p_pred) as fp:
      for line in open(p_truth):
        label = int(line.strip().split(' ')[0])
        pred = float(fp.readline().strip().split(' ')[0])
        if pred not in pred_dict:
            pred_dict[pred] = [0, 0]
        pred_dict[pred][0] += 1
        pred_dict[pred][1] += label

    remain_tot_false = tot_false 
    tot_score = 0.
    for pred in sorted(pred_dict.keys(), key=lambda d:-d):
        imp, clk = pred_dict[pred]
        tot_score += clk * remain_tot_false - clk * (imp-clk) / 2.
        remain_tot_false -= imp - clk
    auc = tot_score / (tot_truth * tot_false)
    print 'AUC= %.6f' % auc 
    return auc

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print '<usage> %s groundtruth prediction' % sys.argv[0]
        exit(1)
    metric(sys.argv[1], sys.argv[2])

