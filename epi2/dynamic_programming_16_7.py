def find_it(name, sequence):
    tmp_name = name
    done = False
    res = ''
    while not done and tmp_name:
        word = sequence[0]
        idx = tmp_name.index(word)
        tmp_name = tmp_name[idx + len(word):]
        if tmp_name:
            res += word
        for j in range(1, len(sequence)):
            if sequence[j] == tmp_name[:len(sequence[j])]:
                tmp_name = tmp_name[len(sequence[j]):]
                res += sequence[j]
            else:
                res = ''
                break

        if j + 1 == len(sequence):
            done = True
        else:
            tmp_name = name[idx + len(word):]

    return res