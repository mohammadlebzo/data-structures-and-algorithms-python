# Challenge Summary
<!-- Description of the challenge -->
Write a function that would implement quick sort algorithm.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![White Board Pic](imgs/quick_sort.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I took an approach that uses recursion and iterations, as for Big O:

- **Time**: O(n log(n)) / as we divide the array into two halves at some point, and take linear time to go through them.
- **Space**: O(log(n)) / as the space here is equal to the height of the recursion tree, which is O(log(n))

## Solution
<!-- Show how to run your code, and examples of it in action -->

In order to run the code enter "**python .\Sorting\quick\quick.py**"

In order to run the tests enter "**pytest .\Sorting\quick\tests\test_quick.py**"
