import collections

class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def compute_lca(node1, node2):
    ''' Compute Lowest Comment Ancestor (LCA) 12.4 '''
    visited = {}
    lca = None

    while not lca:
        lca = visited.get(node1, None) or visited.get(node2, None)
        visited[node1], visited[node2] = node1, node2

        if node1:
            node1 = node1.parent

        if node2:
            node2 = node2.parent

        if not node1 and not node2:
            break

    return lca

def smallest_sub_array(paragraph, keywords):
    ''' Find the smallest subarry covering all values 12.7 '''
    keywords_to_cover = collections.Counter(keywords)
    result = (-1, -1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        # figure out when we have been covered
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1

        while remaining_to_cover == 0:
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)
            p1 = paragraph[left]
            if p1 in keywords:
                keywords_to_cover[p1] += 1
                if keywords_to_cover[p1] > 0:
                    remaining_to_cover += 1
            left += 1

    return result

# def smallest_sub_array_2(paragraph, keywords):
#     ''' Find the smallest subarry covering all values 12.7 '''
#     keyword_counts = {k:0 for k in keywords}
#     candidates = []
#     min_expected, covered = len(keywords), 0
#     l = 0
#     for r, word in enumerate(paragraph):
#         if word in keywords and covered == 0:
#             l = r
#             covered += 1
#         elif word in keywords and covered >= min_expected - 1:
#             candidates.append((l, r))

    



if __name__ == '__main__':
    # a = Node('A')
    # b = Node('B')
    # c = Node('C')
    # d = Node('D')
    # e = Node('E')
    # f = Node('F')
    # g = Node('G')

    # a.left, a.right, b.parent, c.parent = b, c, a, a
    # b.left, b.right, d.parent, f.parent = d, f, b, b
    # f.right, g.parent = g, f

    # print(compute_lca(d, g))

    paragraph = ['apple', 'banana', 'apple', 'apple', 'dog', 'cat', 'apple', 'dog', 'cat', 'apple', 'cat', 'dog']
    keywords = {'banana', 'cat'}
    print(smallest_sub_array(paragraph, keywords))
