#!/usr/bin/env python3

import collections
import sys
# I need to read 3 numbers

names=["Monnei", "Fjee", "Dolladollabilljoll"]

Record = collections.namedtuple("Record", "amount name")

#a = int(input())
#b = int(input())
#c = int(input())

data = map(int, sys.stdin)

# what I want is:
# (a, name[0]), (b, name[1], (c, name[2])

data= zip(data, names)

# but that is ugly, so let us create a namedtuple

data = map(lambda x: Record(*x), data)

# now we have a stream with
# of Records, with fields amount and name

# now find the minimum
result = min(data)
# and print the result
print(result.name)

