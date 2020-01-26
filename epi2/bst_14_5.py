from epi2.binary_tree_9_11 import BinaryTree

def preorder(node):
    def helper(node, coll):
        if node:
            coll.append(node.val)
            helper(node.left, coll)
            helper(node.right, coll)
    coll = []
    helper(node, coll)
    return coll

def postorder(node):
    def helper(node, coll):
        if node:
            helper(node.left, coll)
            helper(node.right, coll)
            coll.append(node.val)
    coll = []
    helper(node, coll)
    return coll

def postorder_build(values):
    def helper(nodes, start, end):
        if end - start + 1 > 1:
            if nodes[end].val > nodes[end - 1].val:
                nodes[end].left = nodes[end - 1]
                helper(nodes, start, end - 1)
            else:
                nodes[end].right = nodes[end - 1]
                mid = end - 2
                if end - start + 1 > 2:
                    while mid >= start and nodes[mid].val > nodes[end].val:
                        mid -= 1

                    if mid >= start:
                        nodes[end].left = nodes[mid]

                helper(nodes, mid + 1, end - 1)
                helper(nodes, start, mid)

    root = None
    if values:
        nodes = [BinaryTree(v) for v in values]
        helper(nodes, 0, len(nodes) - 1)
        root = nodes[-1]

    return root

def preorder_build(values):
    def helper(nodes, start, end):
        if end - start + 1 > 1:
            if nodes[start + 1].val > nodes[start].val:
                nodes[start].right = nodes[start + 1]
                helper(nodes, start + 1, end)
            else:
                nodes[start].left = nodes[start + 1]
                mid = start + 2
                if end - start + 1 > 2:
                    while mid <= end and nodes[mid].val < nodes[start].val:
                        mid += 1

                    if mid <= end:
                        nodes[start].right = nodes[mid]

                helper(nodes, start + 1, mid - 1)
                helper(nodes, mid, end)

    root = None
    if values:
        nodes = [BinaryTree(v) for v in values]
        helper(nodes, 0, len(nodes) - 1)
        root = nodes[0]
        
    return root
