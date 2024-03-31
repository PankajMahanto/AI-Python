from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, node, visited, stack):
        visited[node] = True

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)

        stack.append(node)

    def topological_sort(self):
        visited = {node: False for node in self.graph}
        stack = []

        for node in self.graph:
            if not visited[node]:
                self.topological_sort_util(node, visited, stack)

        return stack[::-1]

# Example usage:
if __name__ == "__main__":
    g = Graph()

    graph_matrix = [
        [0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1]
    ]

    # Convert the matrix to an adjacency list and add edges to the graph
    for i in range(len(graph_matrix)):
        for j in range(len(graph_matrix[0])):
            if graph_matrix[i][j] == 1:
                g.add_edge(i, j)

    # Find the topological order
    top_order = g.topological_sort()

    print("Topological Order:", top_order)
