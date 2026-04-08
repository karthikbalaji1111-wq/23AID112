### DIFFERENCE BETWEEN STACK AND QUEUE



| No | Stack                              | Queue                              |
|----|------------------------------------|------------------------------------|
| 1  | Follows LIFO (Last In First Out)   | Follows FIFO (First In First Out)  |
| 2  | Insertion and deletion at one end  | Insertion at rear, deletion at front |
| 3  | Uses push() and pop()              | Uses enqueue() and dequeue()       |
| 4  | Only one pointer (top)             | Two pointers (front and rear)      |
| 5  | Reverses order of elements         | Maintains original order           |
| 6  | Used in recursion, undo operations | Used in scheduling, buffering      |
| 7  | Example: stack of plates           | Example: queue at ticket counter   |




### Difference Between Binary Tree and Graph

| No | Binary Tree                                  | Graph                                      |
|----|----------------------------------------------|--------------------------------------------|
| 1  | Hierarchical structure                       | Non-hierarchical structure                 |
| 2  | Each node has at most 2 children             | A node can have any number of connections  |
| 3  | Has a single root node                       | No fixed root node                         |
| 4  | No cycles allowed                            | Can have cycles                            |
| 5  | Always connected                             | Can be connected or disconnected           |
| 6  | Used in hierarchical data (like trees)       | Used in networks, maps, social graphs      |
| 7  | Traversals: Inorder, Preorder, Postorder     | Traversals: BFS and DFS                    |


## TIME COMPLEXITY ANALYSIS AMONGST THE DATA STRUCTURES

# Time Complexity Summary (Stack, Queue, Binary Tree, Graph)

| Data Structure | Operation            | Time Complexity |
|----------------|---------------------|-----------------|
| Stack          | Push                | O(1)            |
| Stack          | Pop                 | O(1)            |
| Stack          | Peek (Top)          | O(1)            |
| Stack          | Search              | O(n)            |
| Queue          | Enqueue             | O(1)            |
| Queue          | Dequeue             | O(1)            |
| Queue          | Peek (Front)        | O(1)            |
| Queue          | Search              | O(n)            |
| Binary Tree    | Insertion           | O(n)            |
| Binary Tree    | Deletion            | O(n)            |
| Binary Tree    | Search              | O(n)            |
| Binary Tree    | Traversal           | O(n)            |
| Graph          | Add Vertex          | O(1)            |
| Graph          | Add Edge            | O(1)            |
| Graph          | BFS Traversal       | O(V + E)        |
| Graph          | DFS Traversal       | O(V + E)        |
| Graph          | Search              | O(V + E)        |