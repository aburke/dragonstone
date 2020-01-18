import numpy as np

def compute_square_root(num):
    left, right, mid = 0, num, num/2
    mid_squared = mid*mid
    while not np.isclose(mid_squared, num, rtol = 0.00001):
        if mid_squared > num:
            right = mid
        else:
            left = mid
        mid = (left + right) / 2
        mid_squared = mid * mid

    return round(mid, 4)


if __name__ == "__main__":
    print(compute_square_root(25))
