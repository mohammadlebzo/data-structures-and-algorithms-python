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


def repeated_word(string):
    """
    This function finds the first repeated word within a given string.
    :param string: The string to check
    :return: string
    """
    if len(string.split(" ")) < 2:
        return string

    hash_table = HashTable()
    string_words = "".join(string.lower().split(",")).split(" ")

    for i in string_words:
        hash_table.set(i, "0")
        if len(hash_table.get(i)) > 1:
            return i


if __name__ == "__main__":
    string = "Once upon a time, there was a brave princess who..."
    # string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    # string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    # string = "7"
    # string = ""

    print(repeated_word(string))
