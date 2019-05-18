
def delete_duplicates(arr):
    ''' Delete duplicates 5.5 '''
    if not arr:
        return 0

    write_index = 1
    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1

    for i in range(write_index, len(arr)):
        arr[i] = 0

    return write_index

def remove_item(key, arr):
    ''' Variant 5.5 '''
    if not arr:
        return 0

    sub_index = 0
    for i in range(0, len(arr)):
        if arr[i] != key:
            arr[sub_index] = arr[i]
            sub_index += 1
    
    return sub_index

def two_threshold(m, arr):
    '''Variant 5.5 not completed'''
    occ = 1
    shift = 0
    key = arr[0]

    for i in range(0, len(arr)):
        if occ < m and key == arr[i]:
            arr[i - shift] = arr[i]
            occ += 1
        elif occ == m:
            key = arr[i]
            shift += 1
            arr[i - shift] = arr[i]
        elif key != arr[i]:
            key = arr[i]
            occ = 1
            arr[i - shift] = arr[i]


def show_primes(n):
    ''' Enumerate all primes to n 5.9 '''
    if n == 1:
        return []

    primes = [2]
    for i in range(3, n + 1):
        prime = True
        q = 0
        while primes[q] <= i**0.5:
            if i % primes[q] == 0:
                prime = False
                break

            q += 1

        if prime:
            primes.append(i)
    
    return primes

def show_primes_2(n):
    primes = []
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n):
        if is_prime[p]:
            primes.append(p)

        for i in range(p, n + 1, p):
            is_prime[i] = False

    return primes




if __name__ == "__main__":
    # arr = [1, 2, 2, 2, 7, 9, 9]
    # new_len = delete_duplicates(arr)
    # print(arr[:new_len])

    # arr2 = [1, 1, 9, 3, 1]
    # new_len = remove_item(1, arr2)
    # print(arr2[:new_len])

    # arr3 = [1]
    # new_len = remove_item(1, arr3)
    # print(arr3[:new_len])

    # arr4 = [7, 9, 5, 1]
    # new_len = remove_item(0, arr4)
    # print(arr4[:new_len])

    # arr5 = [1, 2, 2, 2, 4, 4]
    # two_threshold(3, arr5)
    # print(arr5)

    print(show_primes(100))
    print(show_primes_2(100))

