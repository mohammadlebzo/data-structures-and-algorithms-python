# Trees
<!-- Short summary or background information -->
Trees are a non-linear data structure as it doesn't store in a sequential order, it takes a hierarchical structure.

## Challenge
<!-- Description of the challenge -->
- ***Node***
  - Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
- ***Binary Tree***
  - Create a Binary Tree class
    - Define a method for each of the depth first traversals:
    - pre order
    - in order
    - post order which returns an array of the values, ordered appropriately.
- ***Binary Search Tree***
  - Create a Binary Search Tree class
      - This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
        - Add
          - Arguments: value
          - Return: nothing
          - Adds a new node with that value in the correct location in the binary search tree.
        - Contains
          - Argument: value
          - Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I took a recursive approach, as for the Big O:

- For pre_order(), in_order() and post_order():

  - **Time**: O(n)
  - **Space**: O(n)

- For add() and contains():
  
  - **Time**: O(log n)
  - **Space**: O(1)


## API
<!-- Description of each method publicly available in each of your trees -->

- BinaryTree:
  - **pre_order()**: returns tree nodes in the following order: root >> left >> right
  - **in_order()**: returns tree nodes in the following order: left >> root >> right
  - **post_order()**: returns tree nodes in the following order: left >> right >> root
  
- BinaryTree:
  - **add()**: adds a node in the right place in the binary search tree, if less than root the node goes to the left, and if more it goes to the right
  - **contains()**: searches for a value and returns True if found and False if not. 