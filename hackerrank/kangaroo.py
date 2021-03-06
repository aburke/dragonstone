# https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    result = 'NO'
    if (x1 == x2):
        result = 'YES'
    elif (x1 < x2 and v1 > v2) or (x1 > x2 and v1 < v2):
        p1, k1 = (x1 + v1, v1) if x1 < x2 else (x2 + v2, v2)
        p2, k2 = (x1 + v1, v1) if x1 > x2 else (x2 + v2, v2)
        while p1 < p2:
            p1 += k1
            p2 += k2

        if p1 == p2:
            result = 'YES'

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
