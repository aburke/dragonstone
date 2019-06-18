# 14.5 Reconstruct a BST From Traversal Data
class Node(object):

    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{str(self.val)} => ({self.left}, {self.right})"

    def __repr__(self):
        return self.__str__()


def recon_preorder(data):
    if not data:
        return None
    new_root_idx = next((i for i, x in enumerate(data) if data[0] < x), len(data))
    return Node(
        data[0],
        recon_preorder(data[1: new_root_idx]),
        recon_preorder(data[new_root_idx:])
    )
    


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
    
