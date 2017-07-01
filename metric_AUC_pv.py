#!/usr/bin/env python
import random

def metric_AUC(pred_list, label_list):
    tot_truth, tot_false = 0, 0
    for label in label_list:
        if label>0: tot_truth += label
        else: tot_false += 1

    if tot_truth==0 or tot_false==0:
        print 'no truth or false'
        return 0
    if len(pred_list) != len(label_list):
        print 'lens are not equal'
        return 0

    pairs = [(label_list[i], pred_list[i]) for i in xrange(len(pred_list))]
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


def test(p_truth, p_pred):
    label_list, pred_list = [], []
    with open(p_pred) as fp:
      for line in open(p_truth):
        label = int(line.strip().split(' ')[0])
        pred = float(fp.readline().strip().split(' ')[0])
        label_list.append(label)
        pred_list.append(pred)
    metric_AUC(pred_list, label_list)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print '<usage> %s groundtruth prediction' % sys.argv[0]
        exit(1)
    test(sys.argv[1], sys.argv[2])

