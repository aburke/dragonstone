def binarySearch(arr, key, low, high):
    if low <= high and high < len(arr) and low > -1:
        midpoint = low + (high - low)//2
        if arr[midpoint] == key:
            return True
        elif key < arr[midpoint]:
            return binarySearch(arr, key, low, midpoint - 1)
        else:
            return binarySearch(arr, key, midpoint + 1, high)
    return False


def binarySearch2(arr, key):
    low, high = 0, len(arr) - 1
    while high >= 1:
        midpoint = low + (high - low)//2
        if arr[midpoint] == key:
            return True
        if key < arr[midpoint]:
            high = midpoint - 1
        else:
            low = midpoint + 1

    return False
        

if __name__ == "__main__":
    arr = [2, 4, 9, 12, 17, 22, 25, 29, 31, 33]
    # print(binarySearch(arr, 31, 0, len(arr) - 1))
    print(binarySearch2(arr, 33))
