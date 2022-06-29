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

    def length(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

def validate_brackets(passed_str):
    opening_brackets = tuple('({[')
    closing_brackets = tuple(')}]')
    stack = Stack()
    for i in passed_str:
        if i in opening_brackets:
            stack.push(i)
        elif i in closing_brackets:
            position = closing_brackets.index(i)
            if stack.length() > 0 and opening_brackets[position] == stack.top.value:
                stack.pop()
            else:
                return False
    if stack.length() == 0:
        return True
    else:
         return False

if __name__ == "__main__":

    string = "{}"
    print(string, validate_brackets(string))
    string = "{}(){}"
    print(string, validate_brackets(string))
    string = "()[[Extra Characters]]"
    print(string, validate_brackets(string))
    string = "(){}[[]]"
    print(string, validate_brackets(string))
    string = "{}{Code}[Fellows](())"
    print(string, validate_brackets(string))
    string = "[({}]"
    print(string, validate_brackets(string))
    string = "(]("
    print(string, validate_brackets(string))
    string = "{(})"
    print(string, validate_brackets(string))