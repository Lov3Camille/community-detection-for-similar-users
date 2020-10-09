#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
f = open("gplus_combined.txt")
for line in f.readlines():
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    followPair = list(line.split())
    # # increase counters
    celebrity = followPair[0]
    fans = followPair[1]
    # Switch the output format and make follower the key, followee the value
    print('%s\t%s' % (fans, celebrity))

        
