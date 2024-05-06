#!/usr/bin/python
import sys

if len(sys.argv) != 2:
    exit()
f = open(sys.argv[1])
s = f.read()
print(len(s))