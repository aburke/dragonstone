from epi2.bst_14_9 import build_tree
from epi2.binary_tree_9_11 import BinaryTree
from epi2.bst_14_5 import preorder

def test_scenario1():
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tree = build_tree(vals)
    assert [5, 2, 1, 3, 4, 8, 6, 7, 9, 10] == preorder(tree)

def test_scenario2():
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = build_tree(vals)
    assert [5, 2, 1, 3, 4, 7, 6, 8, 9] == preorder(tree)

def test_scenario3():
    vals = []
    tree = build_tree(vals)
    assert tree is None

