#!/usr/bin/env python

def metric(p_truth, p_pred):
    sum_click = 0
    sum_pctr = 0
    with open(p_pred) as fp:
      for line in open(p_truth):
        label = int(line.strip().split(' ')[0])
        pred = float(fp.readline().strip().split(' ')[0])
        sum_click += label
        sum_pctr += pred
    oe = (sum_click + 1e-8) / (sum_pctr + 1e-8)
    print 'OE= %.6f' % oe
    return oe 

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print '<usage> %s groundtruth prediction' % sys.argv[0]
        exit(1)
    metric(sys.argv[1], sys.argv[2])

