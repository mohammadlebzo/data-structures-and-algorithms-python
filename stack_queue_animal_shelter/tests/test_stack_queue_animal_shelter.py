import pytest
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter, Dog, Cat, EmptyStackException

def test_enqueue_one_into_queue(animal_shelter):
    animal_shelter.enqueue(Cat())
    assert animal_shelter.rear.value.kind == "cat"
    assert vars(animal_shelter.rear.value) == {'kind': 'cat'}

def test_enqueue_multiple_into_queue(animal_shelter):
    animal_shelter.enqueue(Cat())
    animal_shelter.enqueue(Cat())
    animal_shelter.enqueue(Dog())
    assert animal_shelter.rear.value.kind == "dog"
    assert vars(animal_shelter.rear.value) == {'kind': 'dog'}
    assert str(animal_shelter) == "{'kind': 'cat'}->{'kind': 'dog'}->{'kind': 'dog'}->{'kind': 'cat'}->{'kind': 'cat'}->{'kind': 'dog'}"

def test_dequeue_one_from_beginning_of_queue(animal_shelter):
    animal_shelter.dequeue("cat")
    assert animal_shelter.front.value.kind == "dog"
    assert vars(animal_shelter.front.value) == {'kind': 'dog'}
    assert str(animal_shelter) == "{'kind': 'dog'}->{'kind': 'dog'}"

def test_dequeue_from_middle_of_queue(animal_shelter):
    animal_shelter.dequeue("dog")
    assert animal_shelter.front.next.value.kind == "dog"
    assert str(animal_shelter) == "{'kind': 'cat'}->{'kind': 'dog'}"

def test_dequeue_where_pref_not_equal_to_dog_nor_cat_from_queue(animal_shelter):
    assert animal_shelter.dequeue("bird") is None

def test_dequeue_empty_queue():
    animal_shelter_empty = AnimalShelter()
    with pytest.raises(EmptyStackException):
        animal_shelter_empty.dequeue("cat")

@pytest.fixture
def animal_shelter():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Cat())
    animal_shelter.enqueue(Dog())
    animal_shelter.enqueue(Dog())
    return animal_shelter