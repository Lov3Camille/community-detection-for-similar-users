#!/usr/bin/env python

from operator import itemgetter
import sys
from collections import Counter

celebrity = None
d = {}
# f = open("facebook_combined.txt")
def get_order_dict_N(_dict, N):
    result = Counter(_dict).most_common(N)
    d = {}
    for k,v in result:
        d[k] = v
    return d


# f = open("facebook_combined.txt")

# input comes from STDIN

# for line in f.readlines():
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    followPair = line.split()
    # parse the input we got from mapper.py
    fans = int(followPair[1])
    d[fans] = []
sys.stdin.seek(0)
# f.seek(0)
# for line in f.readlines():
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    followPair = list(line.split())
    # parse the input we got from mapper.py
    celebrity = int(followPair[0])
    fans = int(followPair[1])
    d[fans].append(celebrity)

for fans in d.keys():
    d2 = {}
    for otherfans in list(d.keys()):
        if otherfans != fans:
            commoncelebrity = list(set(d[fans]).intersection(set(d[otherfans])))
            allcelebrity = list(set(d[fans]).union(set(d[otherfans])))
            similarity = len(commoncelebrity) / len(allcelebrity)
            d2[otherfans] = similarity
    print(list(get_order_dict_N(d2, 4).keys()))

