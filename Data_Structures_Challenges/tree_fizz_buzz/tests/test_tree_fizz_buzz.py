import pytest
from Data_Structures_Challenges.tree_fizz_buzz.tree_fizz_buzz import fizz_buzz_tree, KaryTree, TreeNode


def test_fizz_buzz_on_an_empty_kary_tree(k_tree):
    assert k_tree.root is None


def test_fizz_buzz_on_single_root_kary_tree_with_no_divisible_number(k_tree):
    k_tree.root = TreeNode(1)
    assert k_tree.root.value == 1
    assert fizz_buzz_tree(k_tree) == [1]


def test_fizz_buzz_on_single_root_kary_tree_with_divisible_number(k_tree):
    k_tree.root = TreeNode(15)
    assert k_tree.root.value == 15
    assert fizz_buzz_tree(k_tree) == ['FizzBuzz']


def test_fizz_buzz_on_kary_tree_where_k_is_four_with_no_divisible_numbers(k_tree):
    k_tree.root = TreeNode(1)
    k_tree.root.child.append(TreeNode(2))
    k_tree.root.child.append(TreeNode(11))
    k_tree.root.child.append(TreeNode(4))
    k_tree.root.child.append(TreeNode(13))

    k_tree.root.child[0].child.append(TreeNode(17))
    k_tree.root.child[0].child.append(TreeNode(19))
    k_tree.root.child[0].child.append(TreeNode(7))
    assert fizz_buzz_tree(k_tree) == [17, 19, 2, 7, 11, 4, 1, 13]


def test_fizz_buzz_on_kary_tree_where_k_is_four_with_divisible_numbers(k_tree):
    k_tree.root = TreeNode(1)
    k_tree.root.child.append(TreeNode(2))
    k_tree.root.child.append(TreeNode(3))
    k_tree.root.child.append(TreeNode(4))
    k_tree.root.child.append(TreeNode(15))

    k_tree.root.child[0].child.append(TreeNode(5))
    k_tree.root.child[0].child.append(TreeNode(6))
    k_tree.root.child[0].child.append(TreeNode(7))
    assert fizz_buzz_tree(k_tree) == ['Buzz', 'Fizz', 2, 7, 'Fizz', 4, 1, 'FizzBuzz']


@pytest.fixture
def k_tree():
    k_tree = KaryTree()
    return k_tree
