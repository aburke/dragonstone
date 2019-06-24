def convert_to_alpha(num):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    res = ''
    
    # work in progress
    while num:
        part = num % 26
        part = part or 26
        res += alpha[part - 1]
        num -= 26 if num > 26 else part 

    return res

if __name__ == '__main__':
    print(convert_to_alpha(29))