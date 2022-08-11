import pytest
from Data_Structures_Challenges.tree_intersection.tree_intersection import BinaryTree, TreeNode, HashTable, tree_intersection


def test_common_values_between_two_trees(b1_tree, b2_tree):
    assert tree_intersection(b1_tree, b2_tree) == "100, 125, 160, 175, 200, 350, 500"


def test_output_datatype(b1_tree, b2_tree):
    assert type(tree_intersection(b1_tree, b2_tree)) == type(" ")


@pytest.fixture
def b1_tree():
    b1_tree = BinaryTree()

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

    return b1_tree


@pytest.fixture
def b2_tree():
    b2_tree = BinaryTree()

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

    return b2_tree
