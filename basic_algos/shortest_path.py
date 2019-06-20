class Graph(object):

    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.shortest_path = None

    def get_distance(self, route):
        distance = 0
        if len(route) > 1:
            distance = sum(self.adj_matrix[route[i - 1]][route[i]] for i in range(1, len(route)))
            distance += self.adj_matrix[route[-1]][route[0]]
        
        return distance


def find_shortest_path(path, graph, n):

    for e in (x for x in range(n) if x not in path):
        find_shortest_path(path + [e], graph, n)
    
    if len(path) == n:
        if graph.shortest_path is None or graph.get_distance(path) < graph.get_distance(graph.shortest_path):
            graph.shortest_path = path


def find_path_greedy(path, graph, n):
    
    for i in range(1, n):
        path.append(
            min(
                [(k, x) for k, x in enumerate(graph.adj_matrix[path[i-1]]) if k not in path],
                key = lambda m: m[1]
            )[0]
        )
        
    graph.shortest_path = path


def two_opt(path, trials, graph):
    import numpy as np
    
    for _ in trials:
        vertices = []
        while len(vertices) < 2:
            vert = np.random.randint(2, size = 2)
            if vert not in vertices:
                vertices.append(vert)

        orig_distance = graph.get_distance(path)
        path[vertices[0]], path[vertices[1]] = path[vertices[1]], path[vertices[0]]

        if orig_distance < graph.get_distance(path):
            path[vertices[0]], path[vertices[1]] = path[vertices[1]], path[vertices[0]]

    
        


if __name__ == '__main__':
    adj = [
        [0, 9, 14, 5],
        [9, 0, 4, 2],
        [14, 4, 0, 10],
        [5, 2, 10, 0]
    ]
    
    g = Graph(adj)
    # find_shortest_path([0], g, len(g.adj_matrix))
    find_path_greedy([0], g, len(g.adj_matrix))
    print('Path =>', g.shortest_path)
    print('Distance =>', g.get_distance(g.shortest_path))
