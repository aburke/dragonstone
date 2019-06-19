import queue

class QueueNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class AQueue(object):

    def __init__(self):
        self.top = QueueNode(-1)

    def put(self, val):
        saved = self.top.next
        new_node = QueueNode(val)
        self.top.next = new_node
        new_node.next = saved

    def get(self):
        prev = None
        element = self.top

        while element.next:
            prev = element
            element = element.next
        
        res = None

        if prev:
            prev.next = None
            res = element.val
        
        return res

    def empty(self):
        return self.top.next is None


class Node(object):

    def __init__(self, val):
        self.val = val
        self.nodes = []

    def __str__(self):
        return f'node({str(self.val)})'

    def __repr__(self):
        return self.__str__()


def DFS(root):
    if root:
        print(root.val)
        for n in root.nodes:
            DFS(n)


def BFS(root):
    # work_q = queue.Queue()
    work_q = AQueue()
    work_q.put(root)
    visited = {root: True}
    print(root)
    while not work_q.empty():
        node = work_q.get()
        for n in node.nodes:
            if not visited.get(n, False):
                visited[n] = True
                print(n)
                work_q.put(n)



if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    h = Node(8)
    i = Node(9)

    a.nodes = [b, c, d]
    b.nodes = [e, f]
    c.nodes = [g]
    g.nodes = [h, i]
    e.nodes = [f]
    f.nodes = [c, g]

    # DFS(a)
    BFS(a)