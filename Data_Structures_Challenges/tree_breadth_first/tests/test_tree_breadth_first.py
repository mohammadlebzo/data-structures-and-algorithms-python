import pytest
from tree_breadth_first.tree_breadth_first import BinaryTree, breadth_first, TreeNode


def test_breadth_first_traversal_for_an_empty_tree(b_tree):
    assert breadth_first(b_tree) == []


def test_breadth_first_traversal_for_single_root_tree(b_tree):
    b_tree.root = TreeNode(4)
    assert breadth_first(b_tree) == [4]


def test_breadth_first_traversal_for_a_binary_tree(b_tree):
    b_tree.root = TreeNode(10)
    b_tree.root.left = TreeNode(5)
    b_tree.root.left.left = TreeNode(2)
    b_tree.root.right = TreeNode(15)
    b_tree.root.right.left = TreeNode(14)
    b_tree.root.right.right = TreeNode(30)
    assert breadth_first(b_tree) == [10, 5, 15, 2, 14, 30]


@pytest.fixture
def b_tree():
    b_tree = BinaryTree()
    return b_tree
