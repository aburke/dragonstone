import heapq

def compute_median(sequence):
    ''' Compute the median of online data 10.5 '''
    min_heap = []
    max_heap = []
    switch = False
    
    for e in sequence:
        # largest of the smalles items
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, e))

        if len(max_heap) > len(min_heap):
            # smallest of the largest items
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        median = 0.5 * (min_heap[0] - max_heap[0]) if switch else min_heap[0]
        switch = not switch
        print(median)


if __name__ == '__main__':
    compute_median([1, 0, 3, 5, 2, 0, 1])