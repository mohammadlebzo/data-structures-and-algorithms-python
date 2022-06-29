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
        if not self.top:
            return self.top.value
        else:
            raise EmptyStackException("peek from empty stack is not allowed")

    def __str__(self):
        current = self.top
        items = ''

        while current:
            items += str(current.value) + '\n'
            current = current.next

        return items

class PseudoQueue:
    def __init__(self):
        self.stack_main = Stack()
        self.stack_helper = Stack()

    def enqueue(self, value):
        self.stack_main.push(value)

    def dequeue(self):
        if not self.stack_main.top:
            self.stack_main.pop()
        while self.stack_main.top:
            self.stack_helper.push(self.stack_main.pop())
        popped_data = self.stack_helper.pop()
        while self.stack_helper.top:
            self.stack_main.push(self.stack_helper.pop())

        return popped_data

    def __str__(self):
        item = ''
        current = self.stack_main.top
        while current.next:
            item += f'{{{current.value}}}->'
            current = current.next
        item += f'{{{current.value}}}'
        return item


if __name__ == "__main__":
    pseudo_queue = PseudoQueue()
    print('-------------enqueuing----------------')
    pseudo_queue.enqueue(20)
    pseudo_queue.enqueue(15)
    pseudo_queue.enqueue(10)
    print(pseudo_queue)
    pseudo_queue.enqueue(5)
    print(pseudo_queue)
    print('-------------dequeuing----------------')
    print(pseudo_queue.dequeue())
    print(pseudo_queue)
    print(pseudo_queue.dequeue())
    print(pseudo_queue)
    print('--------------------------------------')


