from collections import namedtuple

SSRange = namedtuple('SSRange', ['i', 'j'])

def slow_search(sub_set, paragraph):
    p = len(sub_set) - 1
    smallest = SSRange(len(paragraph) - 1, 0)
    goal = len(sub_set)
    match_found = False
    while p < len(paragraph):
        j = 0
        for i in range(p, len(paragraph)):
            match_count = len(sub_set.intersection(paragraph[j:i + 1]))
            if match_count == goal and i - j < smallest.i - smallest.j:
                match_found = True
                smallest = SSRange(i, j)
            j += 1

        p += 1

    return smallest if match_found else None
        

def search(sub_set, paragraph):
    j = 0
    smallest = SSRange(len(paragraph) - 1, 0)
    in_s = set()
    goal = len(sub_set)
    for i in range(len(paragraph)):
        word = paragraph[i]
        if word in sub_set and word not in in_s:
            in_s.add(word)
        elif word in sub_set and word in in_s:
            others = in_s - {word}
            while j < i and paragraph[j] not in others:
                j += 1

        if len(in_s) == goal and i - j < smallest.i - smallest.j:
            smallest = SSRange(i, j)

    return None if len(in_s) < goal else smallest


if __name__ == "__main__":
    paragraph = ['a', 'm', 'a', 'm', 'a', 'b', 'm', 'a', 'm', 'b', 'c', 'm', 'm', 'm', 'a', 'b', 'c']
    print(slow_search({'a', 'b', 'c'}, paragraph))
            

