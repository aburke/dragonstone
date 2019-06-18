class Node(object):

    def __init__(self, val):
        self.val = val
        self.nodes = []

def DFS(root):
    if root:
        print(root.val)
        for n in root.nodes:
            DFS(n)


def BFS(root):
    if root:
        item = [root.val]
        item += [x.val for x in root.nodes]



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

    # DFS(a)