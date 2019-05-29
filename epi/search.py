
def find_square_root_v1(num):
    ''' Compute the sqare root 11.5 '''
    if num == 1:
        print(1)
    else:
        threshold = 0.000001
        candidate = num / 2

        while candidate**2 > num:
            candidate = candidate / 2

        addr = candidate / 2
        while num - candidate**2 > threshold:
            if (addr + candidate)**2 <= num:
                candidate += addr

            addr = addr / 2

        print(round(candidate, 6))


def square_root(x):
    ''' Compute the sqare root 11.5 '''
    import numpy as np
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)

    while not np.isclose(left, right):
        mid = 0.5 * (left + right)
        mid_squared = mid * mid

        if mid_squared > x:
            right = mid
        else:
            left = mid

    return left


if __name__ == '__main__':
    find_square_root_v1(25)


    