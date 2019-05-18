import math
from collections import namedtuple

Rectangle = namedtuple('Rectangle', ('x', 'y', 'height', 'width'))

extract_lowest_bit = lambda num : num & ~(num - 1)

remove_lowest_bit = lambda num: num & (num - 1)

def bit_swap(i, j, num):
    '''Brute force swap 4.3'''

    if (num >> i) & 1 != (num >> j) & 1:
        num = num ^ (1 << i | 1 << j)

    return num
    
def br_swap(num):
    '''Brute force swap 4.3'''

    sig = math.floor(math.log(num, 2))
    for i in range((sig + 1) // 2):
        last = sig - i
        num = bit_swap(i, last, num)

    return num

def detect_interserction(r1, r2):
    '''Rectangle intersection 4.11'''

    res = None
    rec_list = [r1, r2]

    min_rx, max_rx = sorted(rec_list, key = lambda r : r.x)
    if min_rx.x + min_rx.width > max_rx.x:
        min_ry, max_ry = sorted(rec_list, key = lambda r : r.y)
        if min_ry.y + min_ry.height > max_ry.y:
            res = Rectangle(
                max_rx.x,
                max_ry.y,
                min(r1.y + r1.height, r2.y + r2.height) - max_ry.y,
                min(r1.x + r1.width, r2.x + r2.width) - max_rx.x
            )

    return res


if __name__ == '__main__':
    num = 121
    print("Binary representation of {}:".format(str(num)), bin(num)[2:])
    print("Extract lowest bit of {}:".format(str(num)), bin(extract_lowest_bit(num))[2:])
    print("Remove lowest bit of {}:".format(str(num)), bin(remove_lowest_bit(num))[2:])
    print("Reversed {}:".format(str(num)), bin(br_swap(num)))

    r1 = Rectangle(2, 4, 5, 12)
    r2 = Rectangle(4, 1, 7, 3)
    print("Intersection of {} and {}:".format(r1, r2), detect_interserction(r1, r2))