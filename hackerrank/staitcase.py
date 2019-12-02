# https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=false

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    c_arr = n * [' ']
    for i in range(-1, -(n + 1), -1):
        c_arr[i] = '#'
        print(''.join(c_arr))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
