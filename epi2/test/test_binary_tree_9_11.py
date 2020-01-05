import epi2.binary_tree_9_11 as btree

def get_nodes():
    return (
        btree.BinaryTree(3),
        btree.BinaryTree(5),
        btree.BinaryTree(9),
        btree.BinaryTree(6),
        btree.BinaryTree(10),
        btree.BinaryTree(11),
        btree.BinaryTree(18),
        btree.BinaryTree(4)
    )

def test_scenario1():
    a, c, d, _, f, g, b, h = get_nodes()
    a.left, a.right, c.parent, g.parent = c, g, a, a
    c.left, c.right, d.parent, f.parent = d, f, c, c
    d.left, b.parent = b, d
    f.left, h.parent = h, f
    expected = [18, 9, 5, 4, 10, 3, 11]
    actual = btree.BinaryTree.inorder(a)
    elmnts = []
    btree.BinaryTree.inorder_recursive(a, elmnts)
    assert expected == actual
    assert actual == elmnts

def test_scenario2():
    a, b, c, _, _, _, _, _ = get_nodes()
    a.left, a.right, b.parent, c.parent = b, c, a, a
    expected = [5, 3, 9]
    actual = btree.BinaryTree.inorder(a)
    elmnts = []
    btree.BinaryTree.inorder_recursive(a, elmnts)
    assert expected == actual
    assert actual == elmnts

def test_scenario3():
    a, b, c, d, _, _, _, _ = get_nodes()
    a.right, b.parent = b, a
    b.right, c.parent = c, b
    c.right, d.parent = d, c
    expected = [3, 5, 9, 6]
    actual = btree.BinaryTree.inorder(a)
    elmnts = []
    btree.BinaryTree.inorder_recursive(a, elmnts)
    assert expected == actual
    assert actual == elmnts

def test_scenario4():
    a, b, c, d, _, _, _, _ = get_nodes()
    a.left, b.parent = b, a
    b.left, c.parent = c, b
    c.left, d.parent = d, c
    expected = [6, 9, 5, 3]
    actual = btree.BinaryTree.inorder(a)
    elmnts = []
    btree.BinaryTree.inorder_recursive(a, elmnts)
    assert expected == actual
    assert actual == elmnts

def test_scenario5():
    a, _, _, _, _, _, _, _ = get_nodes()
    expected = [3]
    actual = btree.BinaryTree.inorder(a)
    elmnts = []
    btree.BinaryTree.inorder_recursive(a, elmnts)
    assert expected == actual
    assert actual == elmnts

def test_scenario6():
    a, b, c, d, e, _, _, _ = get_nodes()
    a.left, a.right, b.parent, c.parent = b, c, a, a
    c.left, d.parent = d, c
    d.left, e.parent = e, d
    expected = [5, 3, 10, 6, 9]
    actual = btree.BinaryTree.inorder(a)
    elmnts = []
    btree.BinaryTree.inorder_recursive(a, elmnts)
    assert expected == actual
    assert actual == elmnts

    
