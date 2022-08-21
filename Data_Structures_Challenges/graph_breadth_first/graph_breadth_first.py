from collections import deque


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)


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

    def breadth_first(self):
        if self.size() == 0:
            return []
        result = []
        visited = set()
        q = Queue()
        start_vertex = [i for i in self.get_nodes()][0]

        q.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(q):
            current_vertex = q.dequeue()

            result.append(current_vertex.value)

            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    q.enqueue(neighbor)
                    visited.add(neighbor)

        return result


if __name__ == "__main__":
    graph = Graph()

    Pandora = graph.add_node('Pandora')
    Arendelle = graph.add_node('Arendelle')
    Metroville = graph.add_node('Metroville')
    Monstroplolis = graph.add_node('Monstroplolis')
    Narnia = graph.add_node('Narnia')
    Naboo = graph.add_node('Naboo')
    graph.add_edge(Pandora, Arendelle)
    graph.add_edge(Arendelle, Metroville)
    graph.add_edge(Arendelle, Monstroplolis)
    graph.add_edge(Metroville, Arendelle)
    graph.add_edge(Metroville, Monstroplolis)
    graph.add_edge(Metroville, Narnia)
    graph.add_edge(Metroville, Naboo)
    graph.add_edge(Monstroplolis, Arendelle)
    graph.add_edge(Monstroplolis, Metroville)
    graph.add_edge(Monstroplolis, Naboo)
    graph.add_edge(Naboo, Narnia)
    graph.add_edge(Naboo, Metroville)
    graph.add_edge(Naboo, Monstroplolis)
    graph.add_edge(Narnia, Naboo)
    graph.add_edge(Narnia, Metroville)

    # print([i for i in graph.get_nodes()][0])
    print(graph.breadth_first())
