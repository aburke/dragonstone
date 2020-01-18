from epi2.binary_tree_9_11 import BinaryTree

def get_lca(n1, n2):
    memory = {n1: {n1}, n2: {n2}}
    intrsc = memory[n1].intersection(memory[n2])
    t1, t2 = n1, n2
    while (t1 or t2) and not intrsc:
        if t1:
            t1 = t1.parent
            memory[n1].add(t1)

        if t2:
            t2 = t2.parent
            memory[n2].add(t2)

        intrsc = memory[n1].intersection(memory[n2])

    return next((x for x in intrsc), None)


if __name__ == "__main__":
    t = {
        1: BinaryTree(1),
        4: BinaryTree(4),
        5: BinaryTree(5),
        8: BinaryTree(8),
        11: BinaryTree(11),
        7: BinaryTree(7),
        12: BinaryTree(12),
        20: BinaryTree(20),
        40: BinaryTree(40),
        13: BinaryTree(13)
    }

    t[1].left, t[1].right, t[4].parent, t[5].parent = t[4], t[5], t[1], t[1]
    t[4].left, t[4].right, t[8].parent, t[11].parent = t[8], t[11], t[4], t[4]
    t[5].left, t[5].right, t[7].parent, t[12].parent = t[7], t[12], t[5], t[5]
    t[7].left, t[7].right, t[20].parent, t[40].parent = t[20], t[40], t[7], t[7]
    t[12].right, t[13].parent = t[13], t[12]

    print(get_lca(t[11], t[7]))
        
