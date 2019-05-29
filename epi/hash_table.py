class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def compute_lca(node1, node2):
    ''' Compute LCA 12.4 '''
    visited = {}
    lca = None

    while not lca:
        lca = visited.get(node1, None) or visited.get(node2, None)
        visited[node1], visited[node2] = node1, node2

        if node1:
            node1 = node1.parent

        if node2:
            node2 = node2.parent

        if not node1 and not node2:
            break

    return lca


if __name__ == '__main__':
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')

    a.left, a.right, b.parent, c.parent = b, c, a, a
    b.left, b.right, d.parent, f.parent = d, f, b, b
    f.right, g.parent = g, f

    print(compute_lca(d, g))
