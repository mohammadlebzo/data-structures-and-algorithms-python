import pytest
from Data_Structures_Challenges.hashmap_left_join.hashmap_left_join import HashTable, left_join


def test_output_of_left_joining_two_hash_maps(hash_table1, hash_table2):
    assert left_join(hash_table1, hash_table2) == [['diligent', 'employed', 'idle'],
                                                   ['fond', 'enamored', 'averse'],
                                                   ['guide', 'usher', 'follow'],
                                                   ['outfit', 'garb', 'NULL'],
                                                   ['wrath', 'anger', 'delight']]


def test_output_data_type_of_left_joining_two_hash_maps(hash_table1, hash_table2):
    assert type(left_join(hash_table1, hash_table2)) == type([])


@pytest.fixture
def hash_table1():
    hash_table1 = HashTable()

    hash_table1.set("diligent", "employed")
    hash_table1.set("fond", "enamored")
    hash_table1.set("guide", "usher")
    hash_table1.set("outfit", "garb")
    hash_table1.set("wrath", "anger")

    return hash_table1


@pytest.fixture
def hash_table2():
    hash_table2 = HashTable()

    hash_table2.set("diligent", "idle")
    hash_table2.set("fond", "averse")
    hash_table2.set("guide", "follow")
    hash_table2.set("flow", "jam")
    hash_table2.set("wrath", "delight")

    return hash_table2
