import pytest
from linked_list.linked_list import LinkedList

def test_empty_linked_list():
    e_list = LinkedList()
    assert e_list.head is None

def test_insert_into_linked_list(l_list):
    l_list.insert(8)
    assert l_list.head.value == 8

def test_head_points_to_the_first_node_in_the_linked_list(l_list):
    assert l_list.head.value == 55

def test_insert_multiple_nodes_into_linked_list(l_list):
    l_list.insert(4)
    l_list.insert(6)
    l_list.insert(12)
    assert l_list.head.value == 12
    assert l_list.head.next.value == 6
    assert l_list.head.next.next.value == 4

def test_if_value_exists_or_not_in_linked_list(l_list):
    assert l_list.includes(9) == True
    assert l_list.includes(20) == False
    assert l_list.includes(4) == False
    assert l_list.includes(10) == True
    assert l_list.includes(55) == True

def test_return_collection_of_all_values_in_linked_list(l_list):
    assert str(l_list) == '{ 55 } -> { 9 } -> { 10 } -> NULL'

@pytest.fixture
def l_list():
    l_list = LinkedList()
    l_list.insert(10)
    l_list.insert(9)
    l_list.insert(55)
    return l_list
