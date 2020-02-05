from epi2.binary_tree_9_11 import BinaryTree
from epi2.bst_14_5 import preorder

def build_tree(sorted_values):
    def helper(start, end):
        node = None
        if start == end:
            node = BinaryTree(sorted_values[start])
        elif start < end:
            mid = (start + end) // 2
            node = BinaryTree(
                sorted_values[mid],
                helper(start, mid - 1),
                helper(mid + 1, end)
            )

        return node

    return helper(0, len(sorted_values) - 1)

if __name__ == "__main__":
    sv = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(preorder(build_tree(sv)))
