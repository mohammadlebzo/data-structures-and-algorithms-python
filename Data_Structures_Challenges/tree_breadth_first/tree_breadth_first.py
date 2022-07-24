class EmptyStackException(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.back = node
            return
        self.back.next = node
        self.back = node

    def dequeue(self):
        if not self.front:
            raise EmptyStackException("dequeue from empty stack is not allowed")
        temp = self.front
        self.front = temp.next
        temp.next = None
        return temp.value


    def __str__(self):
        current = self.front
        items = ''

        while current.next:
            items += f'{{{vars(current.value)}}}->'
            current = current.next

        items += f'{{{vars(current.value)}}}'

        return items
        # return current.value


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


def breadth_first(tree):
    if not tree.root:
        return []

    queue = Queue()
    values = []
    queue.enqueue(tree.root)

    while queue.front:
        front = queue.dequeue()
        values.append(front.value)

        if front.left:
            queue.enqueue(front.left)

        if front.right:
            queue.enqueue(front.right)

    return values


if __name__ == "__main__":
    b_tree = BinaryTree()
    b_tree.root = TreeNode(10)
    b_tree.root.left = TreeNode(5)
    b_tree.root.left.left = TreeNode(2)
    b_tree.root.right = TreeNode(15)
    b_tree.root.right.left = TreeNode(14)
    b_tree.root.right.right = TreeNode(30)
    print(breadth_first(b_tree))
