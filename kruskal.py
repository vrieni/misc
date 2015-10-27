#kruskal's algorithm to find minimum spanning tree

parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()

    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)

    return minimum_spanning_tree




graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': set([
            (1, 'A', 'B'),
            (5, 'A', 'C'),
            (3, 'A', 'D'),
            (4, 'B', 'C'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
        }

undirected_graph_cyclic = {
        'vertices': ['manila', 'singapore', 'zurich',
                        'london', 'new york', 'amsterdam',
                        'paris', 'milan', 'tokyo'],
        'edges': set([
            (1, 'manila', 'singapore'),
            (5, 'manila', 'zurich'),
            (3, 'manila', 'london'),
            (4, 'singapore', 'zurich'),
            (2, 'singapore', 'london'),
            (1, 'zurich', 'london'),
            (2, 'london', 'new york'),
            (1, 'london', 'amsterdam'),
            (2, 'new york', 'amsterdam'),
            (3, 'new york', 'milan'),
            (1, 'milan', 'paris'),
            (2, 'amsterdam', 'paris'),
            (5, 'new york', 'tokyo'),
            (6, 'manila', 'new york'),
            (5, 'tokyo', 'amsterdam'),
            (2, 'tokyo', 'manila')
            ])
}



minimum_spanning_tree = set([
            (1, 'A', 'B'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])

assert kruskal(undirected_graph_cyclic) == minimum_spanning_tree