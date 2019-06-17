def partition(arr, low, high):
	p = left_w = low
	for i in range(low + 1, high):
		if arr[i] < arr[p]:
			arr[i], arr[left_w] = arr[left_w], arr[i]
			left_w += 1
			p = i

	arr[left_w], arr[p] = arr[p], arr[left_w]
	return left_w


def quicksort(arr, low, high):
	if low < high:
		prtn = partition(arr, low, high)
		quicksort(arr, low, prtn)
		quicksort(arr, prtn + 1, high)


if __name__ == '__main__':
    arr = [7, 1, 9, 3, 10]
    quicksort(arr, 0, len(arr))
    print(arr)