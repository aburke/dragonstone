# Work on variants of 9.11

class BinaryTree(object):
    

    def __init__(self, val, left = None, right = None):
        
        self.parent = None
        self.val = val
        self.left = left
        self.right = right

    def inorder_traverse(self, recursive):
        if recursive:
            self._recurse_traverse(self)
        else:
            self._traverse_1(self)

    def _recurse_traverse(self, node):
        if node:
            self._recurse_traverse(node.left)
            print(node.val)
            self._recurse_traverse(node.right)

    def _traverse_1(self, node):
        ''' Implement an inorder traversal in o(1) 9.11 '''
        prev_node, next_node = node.parent, None
        while node:
            if prev_node is node.parent:
                if node.left:
                    next_node = node.left
                else:
                    print(node.val)
                    next_node = node.right or node.parent
            elif prev_node is node.left:
                print(node.data)
                next_node = node.right or node.parent
            else:
                next_node = node.parent

            prev_node, node = node, next_node





            