import pytest
from Data_Structures_Challenges.graph_breadth_first.graph_breadth_first import Graph


def test_breadth_first_traversal_output(graph):
    assert graph.breadth_first() == ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']


def test_breadth_first_traversal_output_type(graph):
    assert type(graph.breadth_first()) == type([])


def test_breadth_first_traversal_output_on_empty_graph(graph_empty):
    assert graph_empty.breadth_first() == []


@pytest.fixture
def graph_empty():
    graph_empty = Graph()
    return graph_empty


@pytest.fixture
def graph():
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

    return graph
