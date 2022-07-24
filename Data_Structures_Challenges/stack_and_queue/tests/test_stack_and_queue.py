import pytest
from stack_and_queue.stack_and_queue import Stack, Queue,EmptyStackException

def test_push_one_onto_stack(stack):
    stack.push(5)
    assert stack.peek() == 5

def test_push_multiple_onto_stack(stack):
    stack.push(5)
    stack.push(6)
    stack.push(9)
    assert stack.peek() == 9
    assert str(stack) == "9\n6\n5\n"

def test_pop_from_stack(stack):
    stack.push(5)
    assert stack.pop() == 5

def test_empty_a_stack_after_multiple_pops(stack):
    stack.push(5)
    stack.push(8)
    stack.pop()
    stack.pop()
    assert stack.is_empty() == True

def test_peek_next_item_on_stack(stack):
    stack.push(5)
    assert stack.peek() == 5

def test_instantiate_empty_stack(stack):
    assert stack

def test_pop_or_peek_empty_stack_and_raise_exception(stack):
    with pytest.raises(EmptyStackException):
        stack.pop()

def test_enqueue_into_queue(queue):
    queue.enqueue(2)
    assert queue.peek() == 2

def test_enqueue_multiple_into_queue(queue):
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(6)
    assert str(queue) == "2\n4\n6\n"

def test_dequeue_expected_value_from_queue(queue):
    queue.enqueue(5)
    assert queue.dequeue() == 5

def test_peek_expected_value_from_queue(queue):
    queue.enqueue(5)
    queue.enqueue(9)
    assert queue.peek() == 5

def test_empty_a_queue_after_multiple_dequeue(queue):
    queue.enqueue(5)
    queue.enqueue(9)
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty() == True

def test_instantiate_empty_queue(queue):
    assert queue

def test_dequeue_or_peek_empty_queue_and_raise_exception(queue):
    with pytest.raises(EmptyStackException):
        queue.dequeue()

@pytest.fixture
def stack():
    stack = Stack()
    return stack

@pytest.fixture
def queue():
    queue = Queue()
    return queue