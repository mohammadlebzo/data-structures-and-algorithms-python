class Vertex:
    """
    The nodes within the graph
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    """
    The connection between to nodes within the graph
    """
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex


class Graph:
    """
    Graph data structure object
    """
    def __init__(self):
        self.__adj_list = {}

    def add_node(self, value):
        """
        Adds a node to the graph
            :param value: the value of the node/vertex
            :return: return the node/vertex
        """
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Adds an edge that connects two nodes within the graph
            :param start_vertex: start point to look for connections
            :param end_vertex: connection target
            :param weight: edge weight
            :return: nothing
        """
        if start_vertex not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex is None:
            edge1 = Edge(end_vertex, weight)
            self.__adj_list[start_vertex].append(edge1)
            return
        if end_vertex not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertex, weight)
        self.__adj_list[start_vertex].append(edge1)

    def get_nodes(self):
        """
        Gets all nodes within the graph
            :return: list of nodes
        """
        return self.__adj_list.keys()

    def size(self):
        """
        Returns the size of the graph, according to the number of nodes within it.
            :return: number
        """
        return len(self.__adj_list)

    def get_neighbors(self, ver):
        """
        Gets all the connections that a passed node has within the graph
        :param ver: the node to find it's connections.
        :return: list of nodes
        """
        return self.__adj_list.get(ver, [])


if __name__ == "__main__":
    graph = Graph()

    a = graph.add_node('A')
    b = graph.add_node('B')
    e = graph.add_node('E')
    c = graph.add_node('C')
    d = graph.add_node('D')
    graph.add_edge(a, b)
    graph.add_edge(b, a)
    graph.add_edge(a, e)
    graph.add_edge(e, a)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    graph.add_edge(b, e)
    graph.add_edge(e, d)
    graph.add_edge(e, c)

    # print(graph.get_nodes())
    # main_arr = [i for i in graph.get_nodes()]
    # print(main_arr[0])
    # print([i.vertex.value for i in graph.get_neighbors(main_arr[2])])
