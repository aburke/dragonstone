class Node:

    def __init__(self, val, node):
        self.val = val
        self.next = node

def even_odd_merge(linked_list):
    odd, even = Node(None, None), Node(None, None)
    o_temp, e_temp = odd, even

    while linked_list:
        if linked_list.val % 2 != 0:
            o_temp.next = linked_list
            o_temp = o_temp.next
        else:
            e_temp.next = linked_list
            e_temp = e_temp.next
    
        linked_list = linked_list.next

    o_temp.next = None
    e_temp.next = odd.next
    return even.next

def view(node):
    node_values = []
    while node:
        node_values.append(str(node.val))
        node = node.next

    return '=>'.join(node_values)
    
    
        
