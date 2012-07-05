#!/usr/bin/env python

import sys

(last_key, sum, count) = (None, 0.0, 0)

for line in sys.stdin:
    (key, value) = line.split('\t')
    if last_key and key != last_key:
        print last_key + '\t' + str(sum/count)
        (sum, count) = (0.0, 0)
        
    last_key = key
    sum += float(value)
    count += 1

if last_key:
    print '%s \t %s' % (last_key, str(sum/count))
