# https://www.hackerrank.com/challenges/day-of-the-programmer/problem?h_r=internal-search

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year < 1918:
        leap = 1 if year % 4 == 0 else 0
        day = 13 - leap
    elif year > 1918:
        leap = 1 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 0
        day = 13 - leap
    else:
        day = 26

    return "{}.09.{}".format(str(day), str(year))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
