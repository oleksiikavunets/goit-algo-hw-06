from graph_analyzer import GraphAnalyzer

graph = {
    'Alice': ['Bob', 'Frank', 'James'],
    'Bob': ['Carol', 'Elly', 'Kelly'],
    'Carol': ['Dan', 'Frank'],
    'Dan': ['Elly', 'Miranda'],
    'Elly': ['Frank', 'Hank', 'James', 'Leo'],
    'Frank': ['Gill'],
    'Gill': ['Dan', 'Frank', 'Hank'],
    'Hank': ['Elly', 'Gill'],
    'Inga': ['Frank', 'Kelly', 'Miranda'],
    'James': ['Gill', 'Kelly'],
    'Kelly': ['Leo'],
    'Leo': ['Kelly', 'Miranda'],
    'Miranda': ['Leo', 'Neo'],
    'Neo': ['Inga']
}

if __name__ == '__main__':
    ga = GraphAnalyzer(graph)
    ga.draw_graph()

    print(ga.number_of_nodes())
    print(ga.number_of_edges())
    print(ga.degree_centrality())
    print(ga.closeness_centrality())
    print(ga.betweenness_centrality())
