
class EmptyQueueException(Exception):
    pass

class Queue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        self.s1.append(item)

    def dequeue(self):
        if self.s2:
            return self.s2.pop()

        if self.s1:
            for _ in range(len(self.s1)):
                self.s2.append(self.s1.pop())

            return self.s2.pop()

        raise EmptyQueueException()

    def is_empty(self):
        return not self.s1 and not self.s2

        
        