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
    functions, to append a value, or insert a new value before or after another value.
    """
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        This function is used to append a new node to the end of the linked list.
        :param value: The value to add(number, string, etc..)
        :return: Nothing
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node

    def insert_before(self, value, new_value):
        """
        This function is used to insert a new node before a specific value in the linked list.
        :param value: The value to find
        :param new_value: The value to insert
        :return: Nothing
        """
        new_node = Node(new_value)
        current = self.head
        if current.value == value:
            new_node.next = self.head
            self.head = new_node
            return

        while current.next is not None:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
                break

            current = current.next

    def insert_after(self, value, new_value):
        """
        This function is used to insert a new node after a specific value in the linked list.
        :param value: The value to find
        :param new_value:The value to insert
        :return: Nothing
        """
        new_node = Node(new_value)
        current = self.head
        while current is not None:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node

            current = current.next

    def __str__(self):
        """
        This function is used to print the entire liked list in a
        specific format.
        :return: String
        """
        temp_list = 'head -> '
        current = self.head

        while current:
            temp_list += f"{{{current.value}}} -> "
            current = current.next

        temp_list += "X"
        return temp_list

if __name__ == '__main__':
    l_list = LinkedList()
    print("---Appending-------------------------------------")
    l_list.append(1)
    print(l_list)
    l_list.append(5)
    print(l_list)
    l_list.append(8)
    print(l_list)
    l_list.append(10)
    print(l_list)
    print("---Inserting Before------------------------------")
    l_list.insert_before(5, 9)
    print(l_list)
    l_list.insert_before(1, 0)
    print(l_list)
    print("---Inserting After-------------------------------")
    l_list.insert_after(5, 7)
    print(l_list)
    l_list.insert_after(10, 17)
    print(l_list)
    print("-------------------------------------------------")
