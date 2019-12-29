from itertools import groupby

def look_n_say(n):
    help_look = lambda seq : ''.join(str(sum(1 for _ in g)) + i for i, g in groupby(seq))
    seq = '1'
    for _ in range(n):
        seq = help_look(seq)
    return seq
