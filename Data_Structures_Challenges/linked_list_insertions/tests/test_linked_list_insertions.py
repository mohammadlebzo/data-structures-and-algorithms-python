import pytest
from Data_Structures_Challenges.linked_list_insertions.linked_list_insertions import LinkedList

def test_adding_new_node_to_linked_list_end(l_list):
    l_list.append(5)
    assert str(l_list) == 'head -> {4} -> {7} -> {9} -> {5} -> X'

def test_adding_multiple_nodes_to_linked_list_end(l_list):
    l_list.append(6)
    l_list.append(10)
    assert str(l_list) == 'head -> {4} -> {7} -> {9} -> {6} -> {10} -> X'

def test_insert_before_node_in_middle_of_linked_list(l_list):
    l_list.insert_before(7, 8)
    assert str(l_list) == 'head -> {4} -> {8} -> {7} -> {9} -> X'

def test_insert_before_first_node_in_linked_list(l_list):
    l_list.insert_before(4, 2)
    assert l_list.head.value == 2
    assert str(l_list) == 'head -> {2} -> {4} -> {7} -> {9} -> X'

def test_insert_after_node_in_middle_of_linked_list(l_list):
    l_list.insert_after(7, 10)
    assert str(l_list) == 'head -> {4} -> {7} -> {10} -> {9} -> X'

def test_insert_after_last_node_in_linked_list(l_list):
    l_list.insert_after(9, 19)
    assert str(l_list) == 'head -> {4} -> {7} -> {9} -> {19} -> X'

@pytest.fixture
def l_list():
    l_list = LinkedList()
    l_list.append(4)
    l_list.append(7)
    l_list.append(9)
    return l_list
