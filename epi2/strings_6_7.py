
digit_map = {
    '1': '',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': '',
    '*': '',
    '#': ''
}

def find_path_helper(all_paths, path, number):
    if len(number) == 0:
        all_paths.append(path)
    else:
        options = digit_map[number[0]]
        if options:
            for letter in digit_map[number[0]]:
                find_path_helper(all_paths, path + letter, number[1:])
        else:
            find_path_helper(all_paths, path, number[1:])


def find_paths(number):
    all_paths = []
    find_path_helper(all_paths, '', number)      
    return all_paths
