
def well_formed_test(brackets):
    ''' Test a String for well-formedness 8.3 '''
    brack_stack, br_lookup = [], {'(': ')', '[': ']', '{': '}'}

    for c in brackets:
        if c in br_lookup:
            brack_stack.append(c)
        elif not brack_stack or br_lookup[brack_stack.pop()] != c:
            return False

    return not brack_stack


class Queue(object):

    def __init__(self):
        ''' Implement Queue using stacks 8.9 '''
        self.input_stack = []
        self.output_stack = []

    def enqueue(self, item):
        self.input_stack.append(item)

    def dequeue(self):
        output = None

        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

        if self.output_stack:
            output = self.output_stack.pop()

        return output