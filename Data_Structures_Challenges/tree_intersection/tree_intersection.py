# ========================= Setup ====================================
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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


class BinaryTree:
    def __init__(self):
        self.root = None

    def in_order(self):
        """
        Returns the tree nodes in the following order: left >> root >> right
        :return: string
        """
        output = []
        if not self.root:
            return self.root

        def _walk(root, out):

            if root.left:
                _walk(root.left, out)

            out.append(root.value)

            if root.right:
                _walk(root.right, out)

        _walk(self.root, output)
        return output


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
# ========================= Setup ====================================


# ========================= The challenge's code ====================================
def tree_intersection(tree1, tree2):
    """
    This function finds the common values between the two trees and returns them.
    :param tree1: first tree
    :param tree2: second tree
    :return: string
    """
    hash_map = HashTable()
    t1 = tree1.in_order()
    t2 = tree2.in_order()
    output = []

    for i in range(len(t1)):
        hash_map.set(str(t1[i]), "0")
        hash_map.set(str(t2[i]), "0")

        if len(hash_map.get(str(t1[i]))) == 2:
            output.append(str(t1[i]))

    return ", ".join(output)
# ========================= The challenge's code ====================================


if __name__ == "__main__":
    b1_tree = BinaryTree()
    b2_tree = BinaryTree()

    b1_tree.root = TreeNode(150)
    b1_tree.root.left = TreeNode(100)
    b1_tree.root.left.left = TreeNode(75)
    b1_tree.root.left.right = TreeNode(160)
    b1_tree.root.left.right.left = TreeNode(125)
    b1_tree.root.left.right.right = TreeNode(175)
    b1_tree.root.right = TreeNode(250)
    b1_tree.root.right.left = TreeNode(200)
    b1_tree.root.right.right = TreeNode(350)
    b1_tree.root.right.right.left = TreeNode(300)
    b1_tree.root.right.right.right = TreeNode(500)

    b2_tree.root = TreeNode(42)
    b2_tree.root.left = TreeNode(100)
    b2_tree.root.left.left = TreeNode(15)
    b2_tree.root.left.right = TreeNode(160)
    b2_tree.root.left.right.left = TreeNode(125)
    b2_tree.root.left.right.right = TreeNode(175)
    b2_tree.root.right = TreeNode(600)
    b2_tree.root.right.left = TreeNode(200)
    b2_tree.root.right.right = TreeNode(350)
    b2_tree.root.right.right.left = TreeNode(4)
    b2_tree.root.right.right.right = TreeNode(500)

    # print(b1_tree.in_order())
    # print(b2_tree.in_order())

    print(tree_intersection(b1_tree, b2_tree))
