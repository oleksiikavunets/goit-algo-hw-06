from itertools import combinations

from graph_analyzer import GraphAnalyzer

graph = {
    'Alice': {'Bob': {'weight': 5}, 'Frank': {'weight': 11}, 'James': {'weight': 3}},
    'Bob': {'Carol': {'weight': 3}, 'Elly': {'weight': 10}, 'Kelly': {'weight': 8}},
    'Carol': {'Dan': {'weight': 4}, 'Frank': {'weight': 2}},
    'Dan': {'Elly': {'weight': 1}, 'Miranda': {'weight': 3}},
    'Elly': {'Frank': {'weight': 2}, 'Hank': {'weight': 4}, 'James': {'weight': 3}, 'Leo': {'weight': 9}},
    'Frank': {'Gill': {'weight': 1}},
    'Gill': {'Dan': {'weight': 2}, 'Frank': {'weight': 3}, 'Hank': {'weight': 5}},
    'Hank': {'Elly': {'weight': 6}, 'Gill': {'weight': 9}},
    'Inga': {'Frank': {'weight': 4}, 'Kelly': {'weight': 7}, 'Miranda': {'weight': 3}},
    'James': {'Gill': {'weight': 2}, 'Kelly': {'weight': 1}},
    'Kelly': {'Leo': {'weight': 1}},
    'Leo': {'Kelly': {'weight': 5}, 'Miranda': {'weight': 3}},
    'Miranda': {'Leo': {'weight': 6}, 'Neo': {'weight': 8}},
    'Neo': {'Inga': {'weight': 2}}
}

if __name__ == '__main__':
    ga = GraphAnalyzer(graph)
    p = ga.dijkstra_path('Alice', 'Neo')

    nodes_pairs = combinations(graph, 2)

    for source, target in nodes_pairs:
        print(f'Path: {source} -> {target}')
        print(ga.dijkstra_path(source, target))
