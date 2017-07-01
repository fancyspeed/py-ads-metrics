#!/usr/bin/env python
#coding: utf-8
import math

bins = 100

def metric(p_truth, p_pred):
    pairs = []
    with open(p_pred) as fp:
      for line in open(p_truth):
        label = int(line.strip().split(' ')[0])
        pctr = float(fp.readline().strip().split(' ')[0])
        pairs.append( (pctr, label) )
    sort_list = sorted(pairs, key=lambda d:d[0])

    oe_list = []
    for i in range(bins):
        part = sort_list[len(sort_list)*i/bins:len(sort_list)*(i+1)/bins]
        sum_pctr = sum([k for k, v in part])
        sum_ctr = sum([v for k, v in part])
        oe = (sum_ctr + 1.) / (sum_pctr + 1.)
        oe_list.append(oe)
    woe = sum(oe_list) / len(oe_list) 
    voe = sum([(v-woe)**2 for v in oe_list]) / len(oe_list) 
    print 'WOE= %.6f, %.6f' % (woe, math.sqrt(voe))
    return woe, voe


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print '<usage> %s groundtruth prediction' % sys.argv[0]
        exit(1)
    metric(sys.argv[1], sys.argv[2])

