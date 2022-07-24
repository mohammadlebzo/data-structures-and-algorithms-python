import pytest
from Data_Structures_Challenges.tree_max.tree_max import BinaryTree, TreeNode

def test_get_max_from_an_empty_tree(b_tree):
    assert b_tree.get_max() == 0

def test_get_max_from_single_root_tree(b_tree):
    b_tree.root = TreeNode(5)
    assert b_tree.get_max() == 5

def test_get_max_from_binary_tree(b_tree):
    b_tree.root = TreeNode(10)
    b_tree.root.left = TreeNode(5)
    b_tree.root.left.left = TreeNode(2)
    b_tree.root.right = TreeNode(15)
    b_tree.root.right.right = TreeNode(30)
    assert b_tree.get_max() == 30

@pytest.fixture
def b_tree():
    b_tree = BinaryTree()
    return b_tree