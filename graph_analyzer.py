import matplotlib.pyplot as plt
import networkx as nx


class GraphAnalyzer:
    def __init__(self, graph: dict):
        self._graph = graph
        self._graph_nx = nx.Graph(self._graph)

    def draw_graph(self):
        nx.draw(self._graph_nx, with_labels=True)
        plt.show()

    def number_of_nodes(self):
        return self._graph_nx.number_of_nodes()

    def number_of_edges(self):
        return self._graph_nx.number_of_edges()

    def degree_centrality(self):
        return nx.degree_centrality(self._graph_nx)

    def closeness_centrality(self):
        return nx.closeness_centrality(self._graph_nx)

    def betweenness_centrality(self):
        return nx.betweenness_centrality(self._graph_nx)

    def bfs(self, source):
        bfs_tree = nx.bfs_tree(self._graph_nx, source)
        return bfs_tree

    def dfs(self, source):
        dfs_tree = nx.dfs_tree(self._graph_nx, source)
        return dfs_tree

    def dijkstra_path(self, source, target):
        return nx.dijkstra_path(self._graph_nx, source, target)
