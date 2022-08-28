import pytest
from Data_Structures_Challenges.graph_depth_first.graph_depth_first import Graph


def test_depth_first_traversal_output(graph):
    assert graph.depth_first([i for i in graph.get_nodes()][0]) == ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']


def test_depth_first_traversal_output_type(graph):
    assert type(graph.depth_first([i for i in graph.get_nodes()][0])) == type([])


def test_depth_first_traversal_output_on_empty_graph(graph_empty):
    assert graph_empty.depth_first() == []


@pytest.fixture
def graph_empty():
    graph_empty = Graph()
    return graph_empty


@pytest.fixture
def graph():
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

    return graph
