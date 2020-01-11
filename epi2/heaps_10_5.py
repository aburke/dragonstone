import heapq

class MedianCalc(object):

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.medians = []
        self.toggle = 0

    def calculate_median(self, val):
        if self.toggle:
            if self.max_heap and val <= self.max_heap[0] * -1:            
                heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -1 * val)
            else:
                heapq.heappush(self.min_heap, val)

            self.medians.append((-1 * self.max_heap[0] + self.min_heap[0]) / 2)
        else:
            if self.min_heap and val >= self.min_heap[0]:
                heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, val)
            else:
                heapq.heappush(self.max_heap, -1 * val)

            self.medians.append(-1 * self.max_heap[0])

        self.toggle ^= 1
