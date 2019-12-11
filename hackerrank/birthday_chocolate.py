# https://www.hackerrank.com/challenges/the-birthday-bar/problem

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    i = 0
    ways = 0  
    while i + m <= len(s):
        if sum(s[i:i + m]) == d:
            ways += 1
        i = i + 1
    return ways

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
