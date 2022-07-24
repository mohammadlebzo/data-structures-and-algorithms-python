import pytest
from Data_Structures_Challenges.trees.trees import BinaryTree, BinarySearchTree, TreeNode

def test_instantiation_of_empty_tree():
    b_tree_empty = BinaryTree()
    assert b_tree_empty
    assert b_tree_empty.root is None

def test_instantiation_of_tree_with_single_root():
    b_tree_single_root = BinaryTree()
    b_tree_single_root.root = TreeNode(10)
    assert b_tree_single_root.root.value == 10

def test_adding_nodes_to_left_and_right_in_binary_search_tree(bs_tree):
    bs_tree.add(5)
    bs_tree.add(15)
    assert bs_tree.pre_order() == '{15}<-{5}<-{10}'

def test_returning_collection_from_preorder(b_tree):
    assert b_tree.pre_order() == '{15}<-{2}<-{5}<-{10}'

def test_returning_collection_from_inorder(b_tree):
    assert  b_tree.in_order() == '{15}<-{10}<-{5}<-{2}'

def test_returning_collection_from_postorder(b_tree):
    assert b_tree.post_order() == '{10}<-{15}<-{5}<-{2}'

def test_value_exist_or_not_in_binary_search_tree(bs_tree):
    bs_tree.add(5)
    bs_tree.add(2)
    bs_tree.add(15)
    assert bs_tree.contains(2) == True
    assert bs_tree.contains(4) == False
    assert bs_tree.contains(10) == True
    assert bs_tree.contains(18) == False

@pytest.fixture
def b_tree():
    b_tree = BinaryTree()
    b_tree.root = TreeNode(10)
    b_tree.root.left = TreeNode(5)
    b_tree.root.left.left = TreeNode(2)
    b_tree.root.right = TreeNode(15)
    return b_tree

@pytest.fixture
def bs_tree():
    bs_tree = BinarySearchTree()
    bs_tree.add(10)
    return bs_tree