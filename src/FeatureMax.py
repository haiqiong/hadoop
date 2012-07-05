#!/usr/bin/env python

import sys

index = int(sys.argv[1])
max = 0

for line in sys.stdin:
    fields = line.strip().split(',')
    if fields[index].isdigit():
        value = int(fields[index])
        if value > max:
            max = value
print max

