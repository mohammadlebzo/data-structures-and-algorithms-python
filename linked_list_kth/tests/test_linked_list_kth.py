import pytest
from linked_list_kth.linked_list_kth import LinkedList

def test_k_greater_than_linked_list_length(l_list):
    with pytest.raises(IndexError):
        l_list.kth_from_end(5)

def test_k_and_linked_list_length_equal_same(l_list):
    with pytest.raises(IndexError):
        l_list.kth_from_end(l_list.get_list_size())

def test_k_not_positive_integer(l_list):
    with pytest.raises(IndexError):
        l_list.kth_from_end(-3)

def test_linked_list_of_size_one():
    l_list_one = LinkedList()
    l_list_one.insert(5)
    assert l_list_one.get_list_size() == 1
    assert l_list_one.kth_from_end(0) == 5

def test_k_in_middle_of_linked_list(l_list):
    assert l_list.kth_from_end(1) == 8

@pytest.fixture
def l_list():
    l_list = LinkedList()
    l_list.insert(2)
    l_list.insert(8)
    l_list.insert(9)
    return l_list
