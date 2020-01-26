import epi2.bst_14_5 as bst
from epi2.binary_tree_9_11 import BinaryTree

def get_nodes():
    return {
        10: BinaryTree(10),
        5: BinaryTree(5),
        2: BinaryTree(2),
        1: BinaryTree(1),
        6: BinaryTree(6),
        20: BinaryTree(20),
        11: BinaryTree(11),
        21: BinaryTree(21)
    }

def test_scenario1():
    b = get_nodes()
    b[10].left, b[10].right = b[5], b[20]
    b[5].left, b[5].right = b[2], b[6]
    b[2].left = b[1]
    b[20].left, b[20].right = b[11], b[21]

    post_order_seq = [1, 2, 6, 5, 11, 21, 20, 10]
    post_order_tree = bst.postorder_build(post_order_seq)

    pre_order_seq = [10, 5, 2, 1, 6, 20, 11, 21]
    pre_order_tree = bst.preorder_build(pre_order_seq)

    assert post_order_seq == bst.postorder(post_order_tree)
    assert pre_order_seq == bst.preorder(pre_order_tree)

def test_scenario2():
    b = get_nodes()
    b[10].left = b[6]
    b[6].left = b[5]
    b[5].left = b[2]
    b[2].left = b[1]

    post_order_seq = [1, 2, 5, 6, 10]
    post_order_tree = bst.postorder_build(post_order_seq)

    pre_order_seq = [10, 6, 5, 2, 1]
    pre_order_tree = bst.preorder_build(pre_order_seq)

    assert post_order_seq == bst.postorder(post_order_tree)
    assert pre_order_seq == bst.preorder(pre_order_tree)

def test_scenario3():
    b = get_nodes()
    b[6].right = b[10]
    b[10].right = b[11]
    b[11].ight = b[20]

    post_order_seq = [20, 11, 10, 6]
    post_order_tree = bst.postorder_build(post_order_seq)

    pre_order_seq = [6, 10, 11, 20]
    pre_order_tree = bst.preorder_build(pre_order_seq)

    assert post_order_seq == bst.postorder(post_order_tree)
    assert pre_order_seq == bst.preorder(pre_order_tree)

def test_scenario4():
    post_order_seq = [10]
    post_order_tree = bst.postorder_build(post_order_seq)

    pre_order_seq = [10]
    pre_order_tree = bst.preorder_build(pre_order_seq)

    assert post_order_seq == bst.postorder(post_order_tree)
    assert pre_order_seq == bst.preorder(pre_order_tree)

def test_scenario5():
    post_order_seq = []
    post_order_tree = bst.postorder_build(post_order_seq)

    pre_order_seq = []
    pre_order_tree = bst.preorder_build(pre_order_seq)

    assert pre_order_tree is None
    assert post_order_tree is None





