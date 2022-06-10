# Singly Linked List
<!-- Short summary or background information -->
A **Singly Linked List** is a sequence of nodes, where each one of them points to the next in line.

## Challenge
<!-- Description of the challenge -->
Create a **Singly Linked List**, that has the following functions:
- An `insert()` function that allows adding a new node to the beginning of the linked list to reach an O(1) Time performance. **Parameters**: value
- An `includes()` function that is used to check if an element is included in the linked list or not. **Parameters**: value
- An `__str__()` function to format the output. (output format: `"{ a } -> { b } -> { c } -> NULL"`).

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Throughout the code I took an iterative approach, because using iteration is faster and less space consuming (mostly).

As for the Big O time and space complexity for the functions, let's look at their averages, except the **insert function**:
- **Time**: O(n)
- **Space**: O(n)

The average time and space complexity for the **insert function** is:
- **Time**: O(1)
- **Space**: O(1)

## API
<!-- Description of each method publicly available to your Linked List -->

- **insert() function**: This function is used to insert a new node to the beginning of the linked list.
- **includes() function**: This function is used to search for an element to find if it's included in the linked list or not.
- **\_\_str\_\_() function**: This function is used to print the entire liked list in a specific format.