class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.max = 0

    def get_max(self):
        """
        Returns the max value in the tree, by traversing the tree in the following order: left >> root >> right,
        then checking if each element's value is bigger than the max of not, if yes the make will store the bigger value, if no it will keep it's value.
        :return: Number
        """
        if not self.root:
            return self.max

        def _walk(root):

            if root.value > self.max:
                self.max = root.value

            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return self.max

if __name__ == "__main__":
    b_tree = BinaryTree()
    b_tree.root = TreeNode(10)
    b_tree.root.left = TreeNode(5)
    b_tree.root.left.left = TreeNode(2)
    b_tree.root.right = TreeNode(15)
    b_tree.root.right.right = TreeNode(30)
    print(b_tree.get_max())
