#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin   :
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    followPair = list(line.split())
    # # increase counters
    celebrity = followPair[1]
    fans = followPair[0]
    # Switch the output format and make follower the key, followee the value
    print('%s\t%s' % (fans, celebrity))

        
