class TreeNode:
    def __init__(self, value):
        self.value = value
        self.child = []


class KaryTree:
    def __init__(self):
        self.root = None


def fizz_buzz_fill(value):
    if value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"
    elif value % 3 == 0:
        return "Fizz"
    elif value % 5 == 0:
        return "Buzz"
    else:
        return value


def fizz_buzz_tree(kary_tree):
    if not kary_tree.root:
        return
    output = []

    def _walk(root):
        if not root.child:
            output.append(fizz_buzz_fill(root.value))
            return

        length = len(root.child)
        for i in range(length - 1):
            _walk(root.child[i])

        output.append(fizz_buzz_fill(root.value))
        _walk(root.child[length - 1])

    _walk(kary_tree.root)
    return output


if __name__ == "__main__":
    k_tree = KaryTree()
    k_tree.root = TreeNode(1)
    k_tree.root.child.append(TreeNode(2))
    k_tree.root.child.append(TreeNode(3))
    k_tree.root.child.append(TreeNode(4))
    k_tree.root.child.append(TreeNode(15))

    k_tree.root.child[0].child.append(TreeNode(5))
    k_tree.root.child[0].child.append(TreeNode(6))
    k_tree.root.child[0].child.append(TreeNode(7))


    print(fizz_buzz_tree(k_tree))

    # Tree:
    #            1
    #       /  /  \  \
    #      2   3   4  15
    #    / | \
    #   5  6  7
    #
    # out: ['Buzz', 'Fizz', 2, 7, 'Fizz', 4, 1, 'FizzBuzz']
