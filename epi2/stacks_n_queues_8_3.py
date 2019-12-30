
def is_well_formed(word):
    stack = []
    matched = True
    options = {']': '[', ')': '(', '}': '{'}
    open_brackets = set(b for b in options.values())
    for c in word:
        if c in open_brackets:
            stack.append(c)
        elif not stack or stack.pop() != options[c]:
            matched = False
            break

    return not stack and matched
