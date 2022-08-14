class Node:
    """
    Node Instructor.
    This class will have only an __init__ method to create nodes.
    """

    def __init__(self, value, next=None):
        """
        Node Constructor.
            :param value: value of the node
            :param next: reference of next node in line
        """
        self.value = value
        self.next = next


class LinkedList:
    """
    A Linked List class with a single head node
    """

    def __init__(self):
        """
        Singly linked list constructor.
        """
        self.head = None

    def insert(self, value):
        """
        This method will insert a node at the start of the linked list
            :param value: Value to insert
            :return: None
        """
        node = Node(value)
        node.next = self.head
        self.head = node


class HashTable:
    """
    HashTable class will have multiple methods, set, get,
    contains, keys and hash.
    It is a data structure that uses keys and values to store
    data to provide easy and fast access to its items.
    """

    def __init__(self, size=1024):
        """
        HashTable constructor.
            :param size: the size of the data structure
        """
        self.__size = size
        self.__buckets = [None] * size
        self.__keys_array = []

    def __hash(self, key):
        """
        This method returns the index in the collection of buckets for that key
            :param key: key to reference can be string, number, etc...
            :return: number
        """

        return sum([ord(i) for i in key]) * 283 % self.__size

    def set(self, key, value):
        """
        this method will  hash the key and set the value and key pair in the buckets, also handling the collisions as needed.
            :param key: key to reference can be string, number, etc...
            :param value: value of the referenced key
            :return: None
        """
        hashed_key = self.__hash(key)
        if self.__buckets[hashed_key] is None:
            hash_list = LinkedList()
            self.__buckets[hashed_key] = hash_list
        self.__keys_array.append(key)
        self.__buckets[hashed_key].insert((key, value))

    def get(self, key):
        """
        Used to find the value that is associated with the passed key.
            :param key: Hash key
            :return: referenced value by passed key
        """
        values = []

        hashed_key = self.__hash(key)
        ll = self.__buckets[hashed_key]
        if ll is None:
            return None

        current = ll.head
        while current:
            if current.value[0] == key:
                values.append(current.value[1])
            current = current.next

        if len(values) > 1:
            return tuple(values)
        else:
            return values[0]

    def contains(self, key):
        """
        Used to find if the value is contained in the Hash Table or not.
            :param key: key to reference can be string, number, etc...
            :return: bool
        """

        if self.get(key):
          return True

        return False

    def keys(self):
        """
        this method will return a collections of all the keys in hashmap as an object
        :return: an array
        """
        return self.__keys_array


def left_join(ht1, ht2):
    output = []

    for i in ht1.keys():
        if i in ht2.keys():
            output.append([i, ht1.get(i), ht2.get(i)])
        else:
            output.append([i, ht1.get(i), "NULL"])

    return output


if __name__ == "__main__":
    hash_table1 = HashTable()
    hash_table2 = HashTable()

    hash_table1.set("diligent", "employed")
    hash_table1.set("fond", "enamored")
    hash_table1.set("guide", "usher")
    hash_table1.set("outfit", "garb")
    hash_table1.set("wrath", "anger")

    hash_table2.set("diligent", "idle")
    hash_table2.set("fond", "averse")
    hash_table2.set("guide", "follow")
    hash_table2.set("flow", "jam")
    hash_table2.set("wrath", "delight")

    print(left_join(hash_table1, hash_table2))
