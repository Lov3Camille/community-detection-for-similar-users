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

for line in sys.stdin:
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

for follower in d.keys():
    d2 = {}
    for otherfollower in list(d.keys()):
        if otherfollower != follower:
            commonfollowees = list(set(d[follower]).intersection(set(d[otherfollower])))
            allfollowees = list(set(d[follower]).union(set(d[otherfollower])))
            similarity = len(commonfollowees) / len(allfollowees)
            d2[str(otherfollower)] = similarity
    d3 = get_order_dict_N(d2, 3)
    print(str(follower) + ": " + " ".join(list(d3.keys())))
#     d3 = get_order_dict_N(d2, 3)
#     for similar_user in d3.keys():
#         common_followees_set = set(d[follower]).intersection(set(d[int(similar_user)]))
#         print(str(follower) + ": " + str(similar_user) + ", " + \
#               str(common_followees_set) + ", " + str(len(common_followees_set)))

