# Queue_and_Deque_python

Data structures implemented in Python (Queue and Deque)

---

# Queue in Data Structures

## 📋 Queue

A **queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle. The first element added is the first one to be removed. Think of it like a line of people waiting — the person who comes first is served first.

---

## Characteristics
- Follows **FIFO** order  
- Insertion (`enqueue`) happens at the **rear (end)**  
- Deletion (`dequeue`) happens at the **front (beginning)**  
- Supports:
  - `enqueue`: add an element to the rear  
  - `dequeue`: remove the element from the front  
  - `peek` or `front`: view the front element without removing it  
  - `is_empty`: check if the queue is empty  

---

## Example (Python)

```python
from collections import deque

queue = deque()

# Enqueue elements
queue.append('a')
queue.append('b')
queue.append('c')

# Peek front element
print(queue[0])  # Output: a

# Dequeue element
print(queue.popleft())  # Output: a
print(queue)            # Output: deque(['b', 'c'])
```
---

## Use Cases

- Task scheduling and management
- Handling requests in servers (e.g., print queue)
- Breadth-first search (BFS) in graphs and trees
- Buffering and asynchronous data transfer

---

# Deque in Data Structures

## 📋 Deque (Double-Ended Queue)

A **deque** is a generalized queue where elements can be added or removed from both ends (front and rear). It combines features of stacks and queues.

---

## Characteristics

- Supports insertion and deletion at both front and rear
- Can function as both FIFO queue and LIFO stack
- Supports:
- append: add to rear
- appendleft: add to front
- pop: remove from rear
- popleft: remove from front
- is_empty: check if empty

---

## Example (Python)

```python
from collections import deque

deque_obj = deque()

# Add elements to rear and front
deque_obj.append('x')
deque_obj.appendleft('y')

print(deque_obj)  # Output: deque(['y', 'x'])

# Remove elements from front and rear
print(deque_obj.popleft())  # Output: y
print(deque_obj.pop())      # Output: x
print(deque_obj)            # Output: deque([])
```

---

## Use Cases

- Implementing both stack and queue functionalities
- Undo/redo operations where elements are added/removed at both ends
- Palindrome checking
- Sliding window algorithms

---

## 🚀 Summary

| Feature            | Queue             | Deque                 |
|--------------------|-------------------|-----------------------|
| Ordering           | FIFO              | Can be FIFO or LIFO   |
| Insertions         | Rear only         | Both front and rear   |
| Deletions          | Front only        | Both front and rear   |
| Indexable          | No                | No                    |
| Use Case Examples  | Task scheduling, BFS | Undo/redo, palindrome, sliding window |
 
---
The attached codes are lists and sets implemented in Python including Circular queue class implemented as an array, maze search function using BFS, Python queue module test, circular deck class inheriting circular queue, priority queue class using unsorted array, strategic maze search function
