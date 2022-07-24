class EmptyStackException(Exception):
    pass
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            raise EmptyStackException("Pop from empty stack is not allowed")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        if not self.is_empty():
            return self.top.value
        else:
            raise EmptyStackException("peek from empty stack is not allowed")

    def is_empty(self):
        return True if self.top is None else False

    def __str__(self):
        current = self.top
        items = ''

        while current:
            items += str(current.value) + '\n'
            current = current.next

        return items

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.back = node
            return
        self.back.next = node
        self.back = node

    def dequeue(self):
        if not self.front:
            raise EmptyStackException("dequeue from empty stack is not allowed")
        temp = self.front
        self.front = temp.next
        temp.next = None
        return temp.value

    def peek(self):
        if not self.is_empty():
            return self.front.value
        else:
            raise EmptyStackException("peek from empty stack is not allowed")

    def is_empty(self):
        return True if self.front is None else False

    def __str__(self):
        current = self.front
        items = ''

        while current:
            items += str(current.value) + '\n'
            current = current.next

        return items


if __name__ == "__main__":
    stack = Stack()
    queue = Queue()

    print("is empty ?", stack.is_empty())
    print("is empty ?", queue.is_empty())
    # print('----------------------------')
    # empty removal exception
    # print(stack.pop())
    # print(queue.dequeue())

    # Adding data
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print('----------------------------')
    print(stack)
    print(queue)
    print('----------------------------')
    # removing data
    print(stack.pop())
    print(queue.dequeue())
    print('----------------------------')
    # peeking
    print(stack.peek())
    print(queue.peek())

