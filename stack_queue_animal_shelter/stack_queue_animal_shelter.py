class EmptyStackException(Exception):
    pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Dog:
    def __init__(self):
        self.kind = 'dog'

class Cat:
    def __init__(self):
        self.kind = 'cat'

class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, animal):
        node = Node(animal)
        if self.front is None:
            self.front = node
            self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self, pref):
        if not self.front:
            raise EmptyStackException("dequeue from empty stack is not allowed")
        if pref.lower() == "dog" or pref.lower() == "cat":
            if self.front.value.kind == pref:
                temp = self.front
                self.front = temp.next
                temp.next = None
                return vars(temp.value)
            else:
                current = self.front
                while current:
                    if current.next == self.rear:
                        temp = current.next
                        current.next = None
                        return vars(temp.value)
                    elif current.next.value.kind == pref:
                        temp = current.next
                        current.next = current.next.next
                        return vars(temp.value)
                    else:
                        current = current.next
        else:
            return None



    def __str__(self):
        current = self.front
        items = ''

        while current.next:
            items += f'{vars(current.value)}->'
            current = current.next

        items += f'{vars(current.value)}'

        return items
        # return current.value


if __name__ == "__main__":
    animal_shelter = AnimalShelter()

    animal_shelter.enqueue(Dog())
    animal_shelter.enqueue(Cat())
    animal_shelter.enqueue(Dog())
    animal_shelter.enqueue(Cat())

    print(animal_shelter)
    # print(animal_shelter.dequeue('dog'))

    print(animal_shelter.dequeue('cat'))
    print(animal_shelter)
    print(animal_shelter.dequeue('dog'))
    print(animal_shelter)
