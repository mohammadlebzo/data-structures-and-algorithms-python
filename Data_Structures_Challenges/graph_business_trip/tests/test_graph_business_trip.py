import pytest
from Data_Structures_Challenges.graph_business_trip.graph_business_trip import Graph, business_trip

nodes_set = []


def test_business_trip_outputting_price(graph):
    assert business_trip(graph, [nodes_set[1], nodes_set[3], nodes_set[5]]) == "$115"
    assert type(business_trip(graph, [nodes_set[1], nodes_set[3], nodes_set[5]])) == type("")


def test_business_trip_outputting_none(graph):
    assert business_trip(graph, [nodes_set[5], nodes_set[0]]) is None
    assert type(business_trip(graph, [nodes_set[0], nodes_set[5]])) == type(None)


@pytest.fixture
def graph():
    graph = Graph()

    Pandora = graph.add_node('Pandora')
    Arendelle = graph.add_node('Arendelle')
    Metroville = graph.add_node('Metroville')
    Monstropolis = graph.add_node('Monstropolis')
    Narnia = graph.add_node('Narnia')
    Naboo = graph.add_node('Naboo')

    nodes_set.append(Pandora)
    nodes_set.append(Arendelle)
    nodes_set.append(Metroville)
    nodes_set.append(Monstropolis)
    nodes_set.append(Narnia)
    nodes_set.append(Naboo)

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

    return graph
