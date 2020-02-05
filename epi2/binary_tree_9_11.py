class BinaryTree(object):

    def __init__(self, val, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return 'BinaryTree({})'.format(self.val)

    @staticmethod
    def inorder_recursive(tree, elmnts):
        if tree:
            BinaryTree.inorder_recursive(tree.left, elmnts)
            elmnts.append(tree.val)
            BinaryTree.inorder_recursive(tree.right, elmnts)

    @staticmethod
    def inorder(tree):
        prev, elmnts = tree, []

        while tree:
            if tree.left and prev is not tree.left and prev is not tree.right:
                prev = tree
                tree = tree.left
            elif tree.left is None and prev is not tree.right:
                elmnts.append(tree.val)
                prev = tree
                tree = tree.right or tree.parent
            elif prev is tree.left:
                elmnts.append(tree.val)
                prev = tree
                tree = tree.right or tree.parent
            elif prev is tree.right:
                prev = tree
                tree = tree.parent

        return elmnts
