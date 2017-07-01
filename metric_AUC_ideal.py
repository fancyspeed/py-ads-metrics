#!/usr/bin/env python

def metric(p_truth):
    feat_dict = {}
    tot_truth, tot_false = 0, 0
    for line in open(p_truth):
        label = int(line.strip().split(' ')[0])
        feat = line.strip().split(' ', 1)[-1]
        if label>0: tot_truth += label
        else: tot_false += 1
        if feat not in feat_dict: feat_dict[feat] = [0, 0]
        feat_dict[feat][0] += 1.
        feat_dict[feat][1] += label 
    if tot_truth==0 or tot_false==0:
        print 'no truth or false'
        return 0

    pairs = []
    for line in open(p_truth):
        label = int(line.strip().split(' ')[0])
        feat = line.strip().split(' ', 1)[-1]
        pred = feat_dict[feat][1] / feat_dict[feat][0]
        pairs.append((label, pred))
    sort_pairs = sorted(pairs, key=lambda d:-d[1])

    remaitot_false = tot_false 
    tot_score = 0.
    for label, pred in sort_pairs:
        if label > 0:
            tot_score += label * remaitot_false
        else:
            remaitot_false -= 1
    auc = tot_score / (tot_truth * tot_false)
    print 'AUC= %.6f' % auc 
    return auc

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print '<usage> %s groundtruth' % sys.argv[0]
        exit(1)
    metric(sys.argv[1])

