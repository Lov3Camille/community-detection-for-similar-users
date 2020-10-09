#/usr/bin/env python3

from operator import itemgetter
import sys
from collections import Counter

same_follwee_list = []
last_follower = None
d = {}
def get_order_dict_N(_dict, N):
    result = Counter(_dict).most_common(N)
    d = {}
    for k,v in result:
        d[k] = v
    return d

f = open("demodataset.txt")
for line in f.readlines():
    line = line.strip()
    cur_follower, cur_followee = line.split()
    cur_follower = int(cur_follower)
    cur_followee = int(cur_followee)

    if cur_follower == last_follower:
        same_follwee_list.append(cur_followee)
    else:
        if last_follower:
            d[last_follower] = []
            d[last_follower] += same_follwee_list

        last_follower = cur_follower
        same_follwee_list = [cur_followee]

if cur_follower == last_follower:
    d[last_follower] = []
    d[last_follower] += same_follwee_list

for cur_follower in d.keys():
    d2 = {}
    max_common_followees = 0
    most_common_follower = None
    for otherfollower in list(d.keys()):
        if otherfollower != cur_follower:
            commonfollowees = list(set(d[cur_follower]).intersection(set(d[otherfollower])))
            if len(commonfollowees) >= max_common_followees:
                max_common_followees = len(commonfollowees)
                most_common_follower = otherfollower
    print(str(cur_follower) + ": " + str(most_common_follower))

