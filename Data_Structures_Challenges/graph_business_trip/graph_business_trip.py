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
        return list(self.__adj_list.keys())

    def size(self):
        return len(self.__adj_list)

    def get_neighbors(self, ver):
        return self.__adj_list.get(ver, [])


def business_trip(graph, cities):
    if len(cities) == 0:
        return None

    result = 0

    for i in range(len(cities) - 1):
        for j in graph.get_neighbors(cities[i]):
            if j.vertex == cities[i + 1]:
                result += j.weight

    if result == 0:
        return None
    else:
        return f"${result}"


if __name__ == "__main__":
    graph = Graph()

    Pandora = graph.add_node('Pandora')
    Arendelle = graph.add_node('Arendelle')
    Metroville = graph.add_node('Metroville')
    Monstropolis = graph.add_node('Monstropolis')
    Narnia = graph.add_node('Narnia')
    Naboo = graph.add_node('Naboo')

    graph.add_edge(Pandora, Arendelle, 150)
    graph.add_edge(Pandora, Metroville, 82)
    graph.add_edge(Arendelle, Pandora, 150)
    graph.add_edge(Arendelle, Metroville, 99)
    graph.add_edge(Arendelle, Monstropolis, 42)
    graph.add_edge(Metroville, Arendelle, 99)
    graph.add_edge(Metroville, Pandora, 82)
    graph.add_edge(Metroville, Monstropolis, 105)
    graph.add_edge(Metroville, Narnia, 37)
    graph.add_edge(Metroville, Naboo, 26)
    graph.add_edge(Monstropolis, Arendelle, 42)
    graph.add_edge(Monstropolis, Metroville, 105)
    graph.add_edge(Monstropolis, Naboo, 73)
    graph.add_edge(Naboo, Narnia, 250)
    graph.add_edge(Naboo, Metroville, 73)
    graph.add_edge(Naboo, Monstropolis, 26)
    graph.add_edge(Narnia, Naboo, 250)
    graph.add_edge(Narnia, Metroville, 37)

    cities_arr = [Arendelle, Monstropolis, Naboo]

    # print(graph.get_neighbors(Pandora)[0].weight)
    print(business_trip(graph, cities_arr))
