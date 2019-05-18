''' Implement Even Odd Merges 7.10 '''

class Node(object):

    def __init__(self, val, ref):
        self.val = val
        self.ref = ref


def create_list(arr):
    top = None
    last = None
    for num in arr:
        if not top:
            top = Node(num, None)
            last = top
        else:
            new_node = Node(num, None)
            last.ref = new_node
            last = new_node

    return top

def traverse(node):
    while node:
        print(node.val)
        node = node.ref

def even_odd_merge_alt(node):
    
    even = Node(None, None)
    odd = Node(None, None)
    last = [even, odd]

    while node:
        last[node.val % 2].ref = node
        last[node.val % 2] = node
        node = node.ref

    last[0].ref = odd.ref
    last[1].ref = None  

    return even.ref

def even_odd_merge(node):
    even = None
    last_even = None
    odd = None
    last_odd = None

    while node:
        if node.val % 2 == 0:
            if even:
                last_even.ref = node
                last_even = node
            else:
                even = node
                last_even = node
        else:
            if odd:
                last_odd.ref = node
                last_odd = node
            else:
                odd = node
                last_odd = node

        node = node.ref

    last_even.ref = odd
    last_odd.ref = None
    

    return even
    


if __name__ == '__main__':
    a_node = create_list([1, 2, 3, 4, 5])
    a_node = even_odd_merge_alt(a_node)
    traverse(a_node)