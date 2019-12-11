# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mnr = mxr = 0
    if len(scores) > 0:
        mn = mx = scores[0]
        for s in scores[1:]:
            if s > mx:
                mxr += 1
                mx = s
            elif s < mn:
                mnr += 1
                mn = s
    return mxr, mnr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
