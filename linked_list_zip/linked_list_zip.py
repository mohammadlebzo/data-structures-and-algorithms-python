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

    def get_list_size(self):
        """
        This function is used to get the size of the linked list.
        :return: list size - number
        """
        counter = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next

        return counter


    def __str__(self):
        """
        This function is used to print the entire liked list in a
        specific format.
        :return: String
        """
        temp_list = ''
        current = self.head

        while current:
            temp_list += f"{{{current.value}}} -> "
            current = current.next

        temp_list += "null"
        return temp_list

def position_swap(current1, current2):
    """
    This function is used for alternating nodes, and storing them in one of the already existing lists .
    :param current1: the first passed node from one of the lists
    :param current2: the second passed node from one of the lists
    :return: nothing
    """
    while current1 is not None and current2 is not None:
        current1_next = current1.next
        current2_next = current2.next

        current2.next = current1_next
        current1.next = current2

        current1 = current1_next
        current2 = current2_next

def zip_lists(l_list1, l_list2):
    """
    This function is used to zip two lists togather, alternating nodes from each of the passed linked lists, and storing them in one of them.
    :param l_list1: First linked list
    :param l_list2: Second linked list
    :return: linked list (in a string representation)
    """
    l_list1_size = l_list1.get_list_size()
    l_list2_size = l_list2.get_list_size()
    l_list1_current = l_list1.head
    l_list2_current = l_list2.head

    if l_list1_size >= l_list2_size:
        position_swap(l_list1_current, l_list2_current)
        return str(l_list1)
    else:
        l_list1_current = l_list2.head
        l_list2_current = l_list1.head.next
        l_list2.insert(l_list1.head.value)

        position_swap(l_list1_current, l_list2_current)
        return str(l_list2)


if __name__ == '__main__':
    l1 = LinkedList()
    l2 = LinkedList()
    print("---------------------------------------------")
    l1.append(1)
    l1.append(3)
    l1.append(2)
    # l1.append(6)
    # l1.append(8)
    l2.append(5)
    l2.append(9)
    l2.append(4)
    # l2.append(6)
    # l2.append(8)
    print(l1)
    print(l2)
    print(zip_lists(l1, l2))
    print("---------------------------------------------")