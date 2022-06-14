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
    functions, to add new nodes and search for the kth node from the tail.
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

    def get_list_size(self):
        """
        This function is used to get the size fo the linked list.
        :return: list size - number
        """
        counter = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next

        return counter

    def kth_from_end(self, k):
        """
        This function is used to find the kth linked list value starting from the tail
        :param k: the num to search for from the tail
        :return: node value
        """
        list_size = self.get_list_size()
        kth_node = (list_size - 1) - k
        current = self.head
        while current is not None:
            if kth_node == 0:
                return current.value
            kth_node -= 1
            current = current.next
        raise IndexError('list index out of range')

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
    print("---------------------------------------------")
    print(l_list)
    l_list.insert(10)
    print(l_list)
    l_list.insert(11)
    print(l_list)
    l_list.insert(12)
    print(l_list)
    l_list.insert(13)
    print(l_list)
    l_list.insert(14)
    print(l_list)
    l_list.insert(15)
    print(l_list)
    print("---------------------------------------------")
    print(l_list.get_list_size())
    print('k of 0 = ', l_list.kth_from_end(0))
    print('k of 1 = ', l_list.kth_from_end(1))
    print('k of 2 = ', l_list.kth_from_end(2))
    print('k of 3 = ', l_list.kth_from_end(3))
    # tests that will raise an Index error exception::
    print("---------------------------------------------")
    print('k of 7 = ', l_list.kth_from_end(7))
    print('k of -3 = ', l_list.kth_from_end(-3))
    print('k of 6 = ', l_list.kth_from_end(l_list.get_list_size()))
    print("---------------------------------------------")