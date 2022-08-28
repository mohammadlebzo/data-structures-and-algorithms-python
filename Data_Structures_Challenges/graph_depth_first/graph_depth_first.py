class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex


class Graph:

    def __init__(self):
        self.__adj_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertex, weight)
        self.__adj_list[start_vertex].append(edge1)

    def get_nodes(self):
        return self.__adj_list.keys()

    def size(self):
        return len(self.__adj_list)

    def get_neighbors(self, ver):
        return self.__adj_list.get(ver, [])

    def depth_first(self, node=None):
        if node is None:
            return []
        result = []
        visited = set()
        stack = []
        start_vertex = node

        stack.append(start_vertex)
        visited.add(start_vertex)

        while len(stack):
            current_vertex = stack.pop()

            result.append(current_vertex.value)

            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

        return result


if __name__ == "__main__":
    graph = Graph()

    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    g = graph.add_node('G')
    h = graph.add_node('H')

    graph.add_edge(a, d)
    graph.add_edge(a, b)
    graph.add_edge(b, a)
    graph.add_edge(b, d)
    graph.add_edge(b, c)
    graph.add_edge(c, b)
    graph.add_edge(c, g)
    graph.add_edge(g, c)
    graph.add_edge(d, a)
    graph.add_edge(d, b)
    graph.add_edge(d, f)
    graph.add_edge(d, h)
    graph.add_edge(d, e)
    graph.add_edge(e, d)
    graph.add_edge(h, d)
    graph.add_edge(h, f)
    graph.add_edge(f, d)
    graph.add_edge(f, h)

    print(graph.depth_first(a))
