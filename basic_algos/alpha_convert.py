def alpha_convert(num):
    converted = ''
    div = 26

    while num:
        converted = chr(num % div - 1 + ord('A')) + converted
        num //= 26

    return converted


if __name__ == "__main__":
    print('9345 =>', alpha_convert(9345))
    print('99 =>', alpha_convert(99))
    print('28 =>', alpha_convert(28))
