#!/usr/bin/env python

import sys

for line in sys.stdin:
    fields = line.split(',')
    if fields[8] and fields[8].isdigit():
        #field[4][1:-1] the country field and skip over records with missing
        #values
        print fields[4][1:-1] + '\t' + fields[8]
