# Stacks and Queues
<!-- Short summary or background information -->
**Stacks** are a sequence of nodes that point to the next in line, which follows the FILO principle.

**Queue** are a sequence of nodes that point to the next in line, which follows the FIFO principle.

## Challenge
<!-- Description of the challenge -->

Create a Stack and Queue classes and implement the following methods:

- **Stack**

    - push
    - pop
    - peek
    - is empty

- **Queue**

    - enqueue
    - dequeue
    - peek
    - is empty


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The approach was a basic implementation of the Stack and Queue, where there is
no loops within the methods to have the best Time and Space complexity, which is:

Big O:
- Time: O(1)
- Space: O(1)

## API
<!-- Description of each method publicly available to your Stack and Queue-->
- Stack methods:
    
    - push(value): Adds the passed value onto the stack.
    - pop(): Removes the top node in the stack, and returns it.
    - peek(): Returns the top node in the stack.
    - is_empty(): Checks if the stack is empty or not, and returns "True" or "False" according to the result.

- Queue methods:
    
    - enqueue(value): Adds the passed value into the queue.
    - dequeue(): Removes the front node in the queue, and returns it.
    - peek(): Returns the front node in the queue.
    - is_empty(): Checks if the queue is empty or not, and returns "True" or "False" according to the result.