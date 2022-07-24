import pytest
from Data_Structures_Challenges.linked_list_zip.linked_list_zip import LinkedList, zip_lists

def test_the_zipping_of_two_equal_in_size_linked_lists(l_list1, l_list2):
    assert zip_lists(l_list1, l_list2) == "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> null"

def test_the_zipping_when_first_linked_list_is_larger_in_size_than_the_second_by_one(l_list1, l_list2):
    l_list1.append(6)
    assert l_list1.get_list_size() > l_list2.get_list_size()
    assert zip_lists(l_list1, l_list2) == "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> {6} -> null"

def test_the_zipping_when_first_linked_list_is_larger_in_size_than_the_second_by_more_than_one(l_list1, l_list2):
    l_list1.append(6)
    l_list1.append(8)
    assert l_list1.get_list_size() > l_list2.get_list_size()
    assert zip_lists(l_list1, l_list2) == "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> {6} -> {8} -> null"

def test_the_zipping_when_second_linked_list_is_larger_in_size_than_the_first_by_one(l_list1, l_list2):
    l_list2.append(6)
    assert l_list2.get_list_size() > l_list1.get_list_size()
    assert zip_lists(l_list1, l_list2) == "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> {6} -> null"

def test_the_zipping_when_second_linked_list_is_larger_in_size_than_the_first_by_more_than_one(l_list1, l_list2):
    l_list2.append(6)
    l_list2.append(8)
    assert l_list2.get_list_size() > l_list1.get_list_size()
    assert zip_lists(l_list1, l_list2) == "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> {6} -> {8} -> null"

@pytest.fixture
def l_list1():
    l_list1 = LinkedList()
    l_list1.append(1)
    l_list1.append(3)
    l_list1.append(2)
    return l_list1

@pytest.fixture
def l_list2():
    l_list2 = LinkedList()
    l_list2.append(5)
    l_list2.append(9)
    l_list2.append(4)
    return l_list2
