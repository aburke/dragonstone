class TrieNode(object):

    def __init__(self):
        self.nodes = [None] * 26
        self.completed = False


class TrieTree(object):

    def __init__(self):
        self.root = TrieNode()

    def get_index(self, c):
        return ord(c) - ord('a')

    def insert(self, word):
        t_node = self.root

        for c in word:
            c = c.lower() 
            idx = self.get_index(c)
            if not t_node.nodes[idx]:
                t_node.nodes[idx] = TrieNode()

            t_node = t_node.nodes[idx]

        if word:
            t_node.completed = True

    def search(self, word):
        t_node = self.root
        exists = False
        stopped_early = False

        for c in word:
            c = c.lower()
            idx = self.get_index(c)
            if t_node.nodes[idx]:
                t_node = t_node.nodes[idx]
            else:
                stopped_early = True
                break

        if word and not stopped_early and t_node.completed:
            exists = True

        return exists


if __name__ == '__main__':
    trie_node = TrieTree()
    trie_node.insert('water')
    trie_node.insert('wait')
    print(trie_node.search('wa'))


        