def remove_duplicates_from_sorted(arr):
    j = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[j-1]:
            arr[j] = arr[i]
            j += 1

    return arr[:j]

if __name__ == "__main__":
    t_arr = [2, 3, 5, 5, 7, 11, 11, 11, 13]
    print(remove_duplicates_from_sorted(t_arr))
    
