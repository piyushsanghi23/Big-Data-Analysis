#!/usr/bin/env python

import sys
import csv


# input comes from STDIN (standard input)
file = csv.reader(sys.stdin)
for line in file:
    # remove leading and trailing whitespace
    # line = line.strip()
    if line[5] == "" and line[4] != "P" and line[6] != "" and (line[2] == 'TMAX' or line[2] == 'TMIN') and line[3] != -9999:
        print '%s\t%s\t%s\t%s' % (line[1], line[0], line[2], line[3])
