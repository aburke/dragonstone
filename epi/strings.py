def phone_number_mnemonics(phone_number):
    ''' Compute all mnemonics for a phone number 6.7 '''

    mnen_map = {
        '0': [''],
        '1': [''],
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z']
    }

    def helper(digits, op):
        if not digits:
            return [op]
        
        res = []
        for l in mnen_map[digits[0]]:
            res.extend(helper(digits[1:], op + l))

        return res

    
    return helper(phone_number, '')

def look_and_say(n):
    ''' The Look-and-Say problem 6.8 '''
    def counter(s):
        count = 1
        key = s[0]
        res = ''
        for i in range(1, len(s)):
            if key != s[i]:
                res += str(count) + key
                key = s[i]
                count = 1
            else:
                count += 1
        res += str(count) + key

        return res

    state = '1'
    for _ in range(1, n):
        state = counter(state)

    return state


def look_and_say_alt(n):
    ''' The Look-and-Say problem 6.8 [pyhonic] '''
    ''' 1, 11, 21, 1211, 111221, 312211'''
    import itertools

    state = '1'
    for _ in range(1, n):
        state = ''.join([str(sum(1 for _ in x)) + i for i, x in itertools.groupby(state)])

    return state

    
if __name__ == '__main__':
    print(phone_number_mnemonics('1298'))