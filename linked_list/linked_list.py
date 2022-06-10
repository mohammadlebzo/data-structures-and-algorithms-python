class Node:
    """
    This class is used to make a new node, with data and a next pointer.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    This class is used to make a linked list, and offer it a couple of
    functions, to add new nodes and search for values.
    """
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        This function is used to insert a new node to the beginning of the linked list.
        :param value: The value to add(number, string, etc..)
        :return: Nothing
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        """
        This function is used to search for an element to find if it's
        included in the linked list or not.
        :param value: The value to find(number, string, etc..)
        :return: Boolean
        """
        current = self.head
        while current is not None:
            if current.value == value:
                return True

            current = current.next

        return False

    def __str__(self):
        """
        This function is used to print the entire liked list in a
        specific format.
        :return: String
        """
        temp_list = ''
        current = self.head

        while current:
            temp_list += f"{{ {current.value} }} -> "
            current = current.next

        temp_list += "NULL"
        return temp_list

if __name__ == '__main__':
    l_list = LinkedList()
    print("---------------------------------------------")
    print(l_list)
    l_list.insert(10)
    print(l_list)
    l_list.insert(5)
    print(l_list)
    l_list.insert(9)
    print(l_list)
    l_list.insert(20)
    print(l_list)
    l_list.insert(25)
    print(l_list)
    l_list.insert(55)
    print(l_list)
    print("---------------------------------------------")
    print('The \"Head\" value is:', l_list.head.value)
    print("---------------------------------------------")
    print('Is Element 9 included ? ', l_list.includes(9))
    print('Is Element 23 included ? ', l_list.includes(23))
    print('Is Element 45 included ? ', l_list.includes(45))
    print('Is Element 25 included ? ', l_list.includes(25))
    print('Is Element 55 included ? ', l_list.includes(55))
    print("---------------------------------------------")