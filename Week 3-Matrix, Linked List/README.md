# Week 3: Matrix, Linked List

## Approach
* Fast and Slow Pointers
    * Definition: Use two pointers traversing an iterable data structure at different speed to identify distinguishable features
    * Use Cases:
        * Detecting cycles in a linked list or sequence
        * Finding the middle element of s linked list
        * Determining if a list is palindromic
        * Finding the meeting point in a cycle
    * Advantages:
        * Efficient for cycle detection without extra space
        * Useful for finding specific elements (like the middle) in a single pass
        * Requires minimal extra space(O(1) space complexity)
    * When to use:
        * Input can be traversed linearly, and
        * Need to identify structure-related traits
* In-place Reversal of a Linked List
    * Definition: Reorganizes the nodes of a linked list in the opposite order directly, without additional memory
    * Use Cases:
        * Reversing an entire singly or doubly linked list
        * Reversing sub-lists within a linked list for pattern matching or reordering
        * Used as a step in more complex algorithms, like palindrome checks
    * Advantages:
        * Space Efficiency: utilizes O(1) space, not requiring extra lists or arrays
        * Time complexity: Achieve O(n) time efficiency by orienting pointers in a single pass
    * When to use:
        * Input is a linked list, and
        * Require list reversal, and
        * Require in-place modification with O(1) space
* Matrices
    * Definition: Operations on a 2D array for numerical calculations
    * Use Cases:
        * Digital image processing (color, brightness, orientation changes)
        * Graph representation via adjacency matrices
        * Dynamic programming for storing subproblem results
        * Grid-based games
    * Advantages:
        * Efficient data organization
        * Versatile application
    * When to use:
        * Input is a 2D array, and
        * It involve matrix operation

## All LeetCode Problems for Week 3 Topics
* Easy: 
    * (234. Palindrome Linked List - In-class Exercise)[Week%203-Matrix,%20Linked%20List/In-class%20Exercise/234.%20Palindrome%20Linked%20List]
    * (876. Middle of the Linked List - Take Home Problems)[Week%203-Matrix,%20Linked%20List/Homework/876.%20Middle%20of%20the%20Linked%20List]
* Medium:
    * (36. Valid Sudoku - Take Home Problems)[Week%203-Matrix,%20Linked%20List/Homework/36.%20Valid%20Sudoku]
    * (48. Rotate Image - In-class Exercise)[Week%203-Matrix,%20Linked%20List/In-class%20Exercise/48.%20Rotate%20Image]
    * (73. Set Matrix Zeroes - In-class Exercise)[Week%203-Matrix,%20Linked%20List/In-class%20Exercise/73.%20Set%20Matrix%20Zeroes]
    * (143. Reorder List - In-class Exercise)[Week%203-Matrix,%20Linked%20List/In-class%20Exercise/143.%20Reorder%20List]
* Hard:
    * (25. Reverse Nodes in k-Group - Take Home Problems)[Week%203-Matrix,%20Linked%20List/Homework/25.%20Reverse%20Nodes%20in%20k-Group]
