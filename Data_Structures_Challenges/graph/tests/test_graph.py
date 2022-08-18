import pytest
from Data_Structures_Challenges.graph.graph import Graph


def test_adding_node_to_graph(graph_empty):
    graph_empty.add_node(5)
    assert graph_empty.size() == 1


def test_adding_edge_to_graph(graph_empty):
    a = graph_empty.add_node(5)
    b = graph_empty.add_node(5)
    graph_empty.add_edge(a, b)
    assert graph_empty.get_neighbors(a)[0].vertex == b


def test_getting_all_nodes_within_graph(graph):
    test_arr = [i.value for i in graph.get_nodes()]
    assert test_arr == ['A', 'B', 'E', 'C', 'D']


def test_getting_all_neighbors_of_node_within_graph(graph):
    main_arr = [i for i in graph.get_nodes()]
    test_arr = [i.vertex.value for i in graph.get_neighbors(main_arr[0])]
    assert test_arr == ['B', 'E', 'C']


def test_getting_all_neighbors_of_node_within_graph_with_their_weights(graph):
    main_arr = [i for i in graph.get_nodes()]
    test_arr = [[i.vertex.value, i.weight] for i in graph.get_neighbors(main_arr[0])]
    assert test_arr == [['B', 0], ['E', 0], ['C', 0]]


def test_getting_size_of_graph(graph):
    assert graph.size() == 5


def test_getting_graph_with_only_one_edge_and_node(graph_empty):
    a = graph_empty.add_node("A")
    graph_empty.add_edge(a, None)
    assert graph_empty.size() == 1
    assert graph_empty.get_neighbors(a)[0].vertex is None


def test_empty_graph(graph_empty):
    assert graph_empty.size() == 0


@pytest.fixture
def graph_empty():
    graph_empty = Graph()
    return graph_empty


@pytest.fixture
def graph():
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

    return graph
