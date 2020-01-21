
class Node(object):

    def __init__(self, val, node = None):
        self.val = val
        self.next = node

def show_all(node):
    rep = ''
    while node:
        rep += '{} => '.format(node.val)
        node = node.next

    return rep

def list_sort(node):
    dummy = Node(None, node)
    sorted_list = Node(None, None)

    while dummy.next:
        saved = dummy.next
        dummy.next = dummy.next.next
        prev, curr = sorted_list, sorted_list.next
        
        while curr and saved.val > curr.val:
            prev = curr
            curr = curr.next

        prev.next, saved.next = saved, curr

    return sorted_list.next
    