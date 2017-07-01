#!/usr/bin/env python
#coding: utf-8
import math

bins = 100

def metric2(p_truth, p_pred):
    # 等分样本的切分方法
    pairs = []
    with open(p_pred) as fp:
      for line in open(p_truth):
        label = int(line.strip().split(' ')[0])
        pctr = float(fp.readline().strip().split(' ')[0])
        pairs.append( (pctr, label) )
    sort_list = sorted(pairs, key=lambda d:d[0])
    v_list = []
    for i in range(bins):
        part = sort_list[len(sort_list)*i/bins:len(sort_list)*(i+1)/bins]
        sum_pctr = sum([k for k, v in part])
        sum_ctr = sum([v for k, v in part])
        diff = float(sum_ctr - sum_pctr) / len(part)
        v_list.append(math.fabs(diff))
    doe = sum(v_list) / len(v_list) 
    voe = sum([(v-doe)**2 for v in v_list]) / len(v_list) 
    print 'DOE= %.6f, %.6f' % (doe, voe)
    return doe

def metric(p_truth, p_pred):
    # 等分pctr区间的切分方法
    pctr_dict = {}
    for i in range(0, bins):
        pctr_dict[i] = [0, 0] # pv, click 
    with open(p_pred) as fp:
      for line in open(p_truth):
        label = int(line.strip().split(' ')[0])
        pctr = float(fp.readline().strip().split(' ')[0])
        pctr = max(0, min(int(pctr * bins), bins-1))
        pctr_dict[pctr][0] += 1
        pctr_dict[pctr][1] += label 

    distances = []
    tot_bin = 0
    for i in range(0, bins):
        pv, click = pctr_dict[i]
        if pv == 0: continue
        tot_bin += 1
        ctr = click/float(pv)
        pctr = (i+0.)/float(bins)
        #print pctr, ctr, pv
        distances.append( math.fabs(ctr - pctr) )
    if not tot_bin: 
        doe = 0
        voe = 0 
    else: 
        doe = sum(distances) / tot_bin
        voe = sum([(v-doe)**2 for v in distances]) / tot_bin
    print 'DOE= %.6f, %.6f' % (doe, voe)
    return doe


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print '<usage> %s groundtruth prediction' % sys.argv[0]
        exit(1)
    metric(sys.argv[1], sys.argv[2])
    #metric2(sys.argv[1], sys.argv[2])

