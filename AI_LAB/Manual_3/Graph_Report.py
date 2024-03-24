class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def is_safe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graph_coloring_util(self, m, color, v):
        if v == self.V:
            return True
        for c in range(1, m+1):
            if self.is_safe(v, color, c):
                color[v] = c
                if self.graph_coloring_util(m, color, v+1):
                    return True
                color[v] = 0

    def graph_coloring(self, m):
        color = [0] * self.V
        if not self.graph_coloring_util(m, color, 0):
            print("Solution does not exist")
            return False

        print("Solution exists:")
        for c in color:
            print(c, end=" ")
        return True


def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        vertices = int(lines[0].strip())
        graph = Graph(vertices)
        for line in lines[1:]:
            edge = list(map(int, line.strip().split()))
            graph.graph[edge[0]][edge[1]] = 1
            graph.graph[edge[1]][edge[0]] = 1
        return graph


if __name__ == "__main__":
    filename = input("Enter the filename containing the graph: ")
    graph = read_graph_from_file(filename)
    num_colors = int(input("Enter the number of colors: "))
    graph.graph_coloring(num_colors)
