# 14.5 Reconstruct a BST From Traversal Data
class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f"{str(self.val)} => ({self.left}, {self.right})"

    def __repr__(self):
        return self.__str__()


def recon_preorder(data):
    nodes = [Node(n) for n in data]
    root = nodes[0]
    i = 1
    for _ in range(1, len(nodes)):
        if nodes[i - 1].val > nodes[i].val:
            nodes[i - 1].left = nodes[i]
            i += 1
        else:
            j = i
            item = nodes[i]
            while j > 0 and item.val > nodes[j - 1].val:
                del nodes[j] 
                j -= 1

            i = j    
            nodes[j].right = item
            del nodes[j]
            

    return root


def preorder_traverse(node, items):
    if node:
        items.append(node.val)
        preorder_traverse(node.left, items)
        preorder_traverse(node.right, items)

def preorder_traverse_2(node):
    if node:
        return [node.val] + preorder_traverse_2(node.left) + preorder_traverse_2(node.right)
    return []
        
        


if __name__ == '__main__':
    a = Node(19)
    b = Node(7)
    c = Node(3)
    d = Node(2)
    e = Node(5)
    f = Node(11)
    g = Node(43)
    h = Node(23)
    i = Node(47)

    a.left, a.right = b, g
    b.left, b.right = c, f
    c.left, c.right = d, e
    g.left, g.right = h, i

    items = preorder_traverse_2(a)
    print(preorder_traverse_2(recon_preorder(items)))

    # items = []
    # print(preorder_traverse_2(a))
    # preorder_traverse(a, items)
    # top = recon_preorder(items)

    # items = []
    # preorder_traverse(top, items)
    # print(items)

    
