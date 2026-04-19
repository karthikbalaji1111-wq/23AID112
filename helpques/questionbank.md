#  DATA STRUCTURES QUESTION BANK

---

#  STACK

## Q1. What is a Stack?
**Answer:**  
A stack is a **linear data structure** that follows **LIFO (Last In First Out)** principle.  
The last inserted element is removed first.

---

## Q2. What are basic operations in stack?
**Answer:**  
- push() → insert element  
- pop() → remove element  
- peek() → view top element  
- isEmpty() → check empty  
- isFull() → check overflow  

---

## Q3. What is stack overflow and underflow?
**Answer:**  
- Overflow: inserting into full stack  
- Underflow: removing from empty stack  

---

## Q4. Applications of stack?
**Answer:**  
- Function calls (call stack)  
- Expression evaluation  
- Undo/Redo  
- Parenthesis checking  

---

## Q5. Array vs Linked list implementation?
**Answer:**  
- Array → fixed size  
- Linked list → dynamic size  

---

## Q6. Time complexity of operations?
**Answer:**  
All operations → O(1)

---

## Q7. What is top pointer?
**Answer:**  
It stores index of last inserted element.

---

## Q8. Infix to postfix conversion use?
**Answer:**  
Uses stack to manage operator precedence.

---

## Q9. Why recursion uses stack?
**Answer:**  
Each function call is stored in stack → maintains execution order.

---

## Q10. What is multiple stack?
**Answer:**  
Two stacks can share same array for efficient memory use.

---

#  QUEUE 

## Q1. What is a Queue?
**Answer:**  
A queue is a linear structure following **FIFO (First In First Out)**.

---

## Q2. Operations of queue?
**Answer:**  
- enqueue() → insert  
- dequeue() → remove  
- front() → first element  
- rear() → last element  

---

## Q3. What is overflow/underflow?
**Answer:**  
- Overflow → queue full  
- Underflow → queue empty  

---

## Q4. Types of queue?
**Answer:**  
- Simple queue  
- Circular queue  
- Priority queue  
- Deque  

---

## Q5. Circular queue advantage?
**Answer:**  
Efficient memory use (no wastage of space)

---

## Q6. Time complexity?
**Answer:**  
All operations → O(1)

---

## Q7. What is priority queue?
**Answer:**  
Elements are removed based on priority, not order.

---

## Q8. Difference: stack vs queue?
**Answer:**  
- Stack → LIFO  
- Queue → FIFO  

---

## Q9. Applications?
**Answer:**  
- CPU scheduling  
- Printer queue  
- BFS traversal  

---

## Q10. What is deque?
**Answer:**  
Double-ended queue → insertion & deletion from both ends

---

# 🌳 BINARY TREE (10 Questions + Answers)

## Q1. What is a Binary Tree?
**Answer:**  
A tree where each node has **at most 2 children**.

---

## Q2. Types of binary trees?
**Answer:**  
- Full  
- Complete  
- Perfect  
- Balanced  

---

## Q3. What is height of tree?
**Answer:**  
Number of edges from root to deepest node.

---

## Q4. Traversals?
**Answer:**  
- Inorder (LNR)  
- Preorder (NLR)  
- Postorder (LRN)  

---

## Q5. What is BST?
**Answer:**  
Left < Root < Right property

---

## Q6. Time complexity (search in BST)?
**Answer:**  
- Best → O(log n)  
- Worst → O(n)  

---

## Q7. What is leaf node?
**Answer:**  
Node with no children

---

## Q8. What is balanced tree?
**Answer:**  
Height difference ≤ 1 for all nodes

---

## Q9. What is complete tree?
**Answer:**  
All levels filled except last (left filled)

---

## Q10. Applications?
**Answer:**  
- Searching  
- Expression trees  
- Hierarchical data  

---

#  GRAPH 

## Q1. What is a graph?
**Answer:**  
A set of **vertices (nodes)** and **edges (connections)**.

---

## Q2. Types of graphs?
**Answer:**  
- Directed  
- Undirected  
- Weighted  
- Unweighted  

---

## Q3. What is degree of node?
**Answer:**  
Number of edges connected to node

---

## Q4. What is BFS?
**Answer:**  
Breadth First Search → level-wise traversal using queue

---

## Q5. What is DFS?
**Answer:**  
Depth First Search → goes deep using stack/recursion

---

## Q6. Difference BFS vs DFS?
**Answer:**  
- BFS → queue  
- DFS → stack  

---

## Q7. What is adjacency matrix?
**Answer:**  
2D matrix representation of graph

---

## Q8. What is adjacency list?
**Answer:**  
List storing neighbors of each node

---

## Q9. What is cycle?
**Answer:**  
Path that starts and ends at same node

---

## Q10. Applications?
**Answer:**  
- Network routing  
- Social networks  
- Maps  

---

