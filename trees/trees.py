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
        """
        Adds a new node to the stack as the top.
        :param value: value to add
        :return: nothing
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def __str__(self):
        """
        Formatting the stack
        :return: string
        """
        current = self.top
        items = ''

        items += f'{{{current.value}}}'

        while current.next:
            items += f'<-{{{current.next.value}}}'
            current = current.next

        return items

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        Returns the tree nodes in the following order: root >> left >> right
        :return: string
        """
        output = Stack()
        if not self.root:
            return self.root

        def _walk(root, out):
            out.push(root.value)

            if root.left:
                _walk(root.left, out)

            if root.right:
                _walk(root.right, out)

        _walk(self.root, output)
        return str(output)

    def in_order(self):
        """
        Returns the tree nodes in the following order: left >> root >> right
        :return: string
        """
        output = Stack()
        if not self.root:
            return self.root

        def _walk(root, out):

            if root.left:
                _walk(root.left, out)

            out.push(root.value)

            if root.right:
                _walk(root.right, out)

        _walk(self.root, output)
        return str(output)

    def post_order(self):
        """
        Returns the tree nodes in the following order: left >> right >> root
        :return: string
        """
        output = Stack()
        if not self.root:
            return self.root

        def _walk(root, out):
            if root.left:
                _walk(root.left, out)

            if root.right:
                _walk(root.right, out)

            out.push(root.value)

        _walk(self.root, output)
        return str(output)

class BinarySearchTree(BinaryTree):

    def add(self, value):
        """
        Adds a new tree node, by looking if the value is more or less than the root, if less go left, if more go right.
        :param value: value to add
        :return: Nothing
        """
        if not self.root:
            self.root = TreeNode(value)
            return
        def _walk(root):
            if value < root.value:
                if root.left:
                    _walk(root.left)
                else:
                    root.left = TreeNode(value)
            if value > root.value:
                if root.right:
                    _walk(root.right)
                else:
                    root.right = TreeNode(value)
            if value == root.value:
                root.right = TreeNode(value)
        _walk(self.root)

    def contains(self, value):
        """
        Checks if a value is included in the tree, if yes return true, if no return false.
        :param value: Value to search for
        :return: Boolean
        """
        if not self.root:
            return False
        if self.root.value == value:
            return True
        def _walk(root, key):
            if root is None or root.value == key:
                return root

                # Key is greater than root's key
            if root.value < key:
                return _walk(root.right, key)

                # Key is smaller than root's key
            return _walk(root.left, key)

        if _walk(self.root, value):
            if _walk(self.root, value).value == value:
                return True
        else:
            return False


if __name__ == "__main__":
    b_tree = BinaryTree()
    bs_tree = BinarySearchTree()

    b_tree.root = TreeNode(10)
    b_tree.root.left = TreeNode(5)
    b_tree.root.left.left = TreeNode(2)
    b_tree.root.right = TreeNode(15)

    print('------------pre order-------------------')
    print(b_tree.pre_order())
    print('-------------in order-------------------')
    print(b_tree.in_order())
    print('-----------post order-------------------')
    print(b_tree.post_order())
    print('------------adding to bsTree--------------')
    bs_tree.add(10)
    print(bs_tree.pre_order())
    bs_tree.add(5)
    print(bs_tree.pre_order())
    bs_tree.add(2)
    print(bs_tree.pre_order())
    bs_tree.add(11)
    print(bs_tree.pre_order())
    bs_tree.add(3)
    print(bs_tree.pre_order())
    print('------------searching bsTree--------------')
    print('Is 9 available? ', bs_tree.contains(9))
    print('Is 3 available? ', bs_tree.contains(3))
    print('------------------------------------------')
