def find_duplicate_and_missing(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    for i in range(1, n):
        if sorted_arr[i] == sorted_arr[i - 1]:
            break

    missing = n * (n - 1) * 0.5 + i - sum(arr)
    return i, int(missing)


if __name__ == "__main__":
    arr = [0, 1, 2, 5, 5, 4]
    print(find_duplicate_and_missing(arr))