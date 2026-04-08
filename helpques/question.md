## Stack and Queue questions 


###### STACK

## Question 1
You are building a simple text editor like Notepad. Every time the user types a word, it gets stored. When the user clicks 'Undo', the last typed word should be removed.

## Theory
A stack follows LIFO (Last In, First Out). The last element pushed is the first to be popped. It is like a pile of books in which the book whih is kept in the last is kept on the top and the first to be removed. So always the last element which is put inside a stack is the first to move out. This is highly favourable in this case because the last typed word is in the top of the stack and by using the pop function whicu is termed as undo the top word aka the last typed word will be removed.


Operations used:
- push() -> store word
- pop() -> undo last word

## Time and Space Complexity
- Push: O(1)  
- Pop: O(1)  
- Space: O(n)



## Code 

```python
stack = []

def type_word(word):
    stack.append(word)       
    print("Typed:", word)

def undo():
    if stack:
        removed = stack.pop()  
        print("Undone:", removed)
    else:
        print("Nothing to undo!")

type_word("Hello")
type_word("World")
undo()       
print(stack) 

```




## Question 2

## Stock Span Analysis


### Problem
Given daily stock prices, find the span of each day.  
Span = number of consecutive days before it (including today) where price was less than or equal to today’s price.

Example:
Prices: [100, 80, 60, 70, 60, 75, 85]  
Span:   [1,   1,  1,  2,  1,  4,  6]



### Theory
Stack is used to keep track of indices of days. We use LIFO to remove smaller elements and find span efficiently by subtracting the indexes whih are stored in the stack by the latest current element.

Span = maximum number of consecutive days before today such that price <= today's price.

Span[i] = i - previous higher index  
If no previous higher → span[i] = i + 1  



### Code (Python)

```python
data = [100, 80, 60, 70, 85]
n = len(data)

stack = []
span = [0] * n

for i in range(n):
    while len(stack) > 0 and data[stack[-1]] <= data[i]:
        stack.pop()

    if len(stack) == 0:
        span[i] = i + 1
    else:
        span[i] = i - stack[-1]

    stack.append(i)

print(span)
```





## Question 3 

# Next Greater Element

## Problem
Find the next greater element for each element in the array.   If no greater element exists, return -1.


## Theory
Stack stores only those elements which have chances to be greater.  
We remove smaller elements using stack and find the next greater efficiently.


## Time Complexity
O(n)


## Code (Python)

```python
def nge(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()

        if len(stack) > 0:
            result[i] = stack[-1]
        else:
            result[i] = -1

        stack.append(arr[i])

    return result


arr = [4, 5, 2, 10]
print(nge(arr))
```





## Question 4

# Valid Parenthesis

## Problem
Check if a string containing brackets is valid.  Valid means every opening bracket has a matching closing bracket in correct order.


## Theory
Stack is used to store opening brackets.  
When a closing bracket comes, we check the top of the stack.



## Time Complexity
O(n)


## Code (Python)


```python
def valid(s):
    stack = []

    for i in s:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False

            top = stack[-1]

            if (i == ')' and top == '(') or \
               (i == ']' and top == '[') or \
               (i == '}' and top == '{'):
                stack.pop()
            else:
                return False

    return len(stack) == 0


s = input("Enter: ")

if valid(s):
    print("ok")
else:
    print("no")

```





## Question 5 


# Palindrome using Stack

## Problem
Check whether a given word is a palindrome using stack.  
A palindrome reads the same forward and backward.


## Theory
Stack follows LIFO.  
By pushing all characters and popping them, we get the reverse of the word.



## Time Complexity
O(n)





## Code (Python)

```python
class Stack:
    def __init__(self):
        self.values = []

    def push(self, x):
        self.values.append(x)

    def pop(self):
        return self.values.pop()

    def empty(self):
        return len(self.values) == 0


def operation(word):
    s = Stack()

    for k in word:
        s.push(k)

    ans = ""

    while not s.empty():
        ans += s.pop()

    if word == ans:
        print("Palindrome")
    else:
        print("Not palindrome")


word = input("Enter word: ")
operation(word)
```



##### QUEUE




### Question 1 




## Implement Stack using Queue

### Problem
Implement a stack using queue operations.



## Theory
Stack follows LIFO, but queue follows FIFO.  We simulate stack by rearranging elements in queue.



## Time Complexity
Push: O(n)  
Pop: O(1)



## Code (Python)

```python
from collections import deque

class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        if self.q:
            return self.q.popleft()
        return None


s = Stack()
s.push(10)
s.push(20)
print(s.pop())

```

## Question 2 


# Queue using Stack

## Problem
Implement a queue using stack operations.



## Theory
Queue follows FIFO (First In First Out).  Stack follows LIFO (Last In First Out).  We use two stacks to reverse the order and simulate queue behavior.



## Time Complexity
Enqueue: O(1)  
Dequeue: O(n)


## Code (Python)

```python
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack1:
            return None

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        value = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return value


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
```

## Question 3 



# Queue using Stack

## Problem
Implement a queue using stack operations.



## Theory
Queue follows FIFO (First In First Out).  
Stack follows LIFO (Last In First Out).  
We use two stacks to reverse the order and simulate queue behavior.



## Time Complexity
Enqueue: O(1)  
Dequeue: O(n)

## Code (Python)

```python
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack1:
            return None

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        value = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return value


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
```

## Question 4 



## Call Center Support System using Queue

### Problem
A customer support center receives calls. Each customer is handled in the order they arrive.  
Simulate the system where:
- New customer → added to queue  
- Customer served → removed from queue  



## Theory
Queue follows FIFO (First In First Out), so the first customer gets served first.



## Time Complexity
Enqueue: O(1)  
Dequeue: O(1)



## Code (Python)

```python
from collections import deque

queue = deque()

def add_customer(name):
    queue.append(name)
    print("Added:", name)

def serve_customer():
    if queue:
        print("Served:", queue.popleft())
    else:
        print("No customers")


add_customer("A")
add_customer("B")
add_customer("C")

serve_customer()
serve_customer()
```

## Question 5



 Traffic Signal Management System

### Problem
Vehicles arrive at a traffic signal and wait in a line.  
When the signal turns green, vehicles pass one by one in the order they arrived.



## Theory
Queue follows FIFO (First In First Out), so vehicles move in the same order they arrive.

## Time Complexity
Enqueue: O(1)  
Dequeue: O(1)



## Code (Python)

```python
from collections import deque

queue = deque()

def vehicle_arrives(name):
    queue.append(name)
    print("Arrived:", name)

def signal_green():
    if queue:
        print("Passed:", queue.popleft())
    else:
        print("No vehicles")


vehicle_arrives("Car")
vehicle_arrives("Bike")
vehicle_arrives("Bus")

signal_green()
signal_green()
signal_green()
```




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





