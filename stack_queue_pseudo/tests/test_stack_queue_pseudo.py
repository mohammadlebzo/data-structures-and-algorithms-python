import pytest
from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue, EmptyStackException

def test_enqueue_one_item_to_queue(pseudo_queue):
    pseudo_queue.enqueue(5)
    assert pseudo_queue.stack_main.top.value == 5
    assert str(pseudo_queue) == '{5}->{10}->{15}->{20}'

def test_enqueue_multiple_to_queue(pseudo_queue):
    pseudo_queue.enqueue(5)
    pseudo_queue.enqueue(1)
    assert pseudo_queue.stack_main.top.value == 1
    assert pseudo_queue.stack_main.top.next.value == 5
    assert str(pseudo_queue) == '{1}->{5}->{10}->{15}->{20}'

def test_dequeue_one_from_queue(pseudo_queue):
    pseudo_queue.dequeue()
    assert str(pseudo_queue) == '{10}->{15}'

def test_dequeue_multiple_from_queue(pseudo_queue):
    pseudo_queue.dequeue()
    pseudo_queue.dequeue()
    assert str(pseudo_queue) == '{10}'

def test_dequeue_empty_queue():
    pseudo_queue_empty = PseudoQueue()
    with pytest.raises(EmptyStackException):
        pseudo_queue_empty.dequeue()

@pytest.fixture
def pseudo_queue():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(20)
    pseudo_queue.enqueue(15)
    pseudo_queue.enqueue(10)
    return pseudo_queue
