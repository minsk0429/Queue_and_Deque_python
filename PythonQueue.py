import queue

Q = queue.Queue(maxsize=20)

for v in range(1, 10):
    Q.put(v)
print("Queue contents: ", end='')
for _ in range(1, 10):
    print(Q.get(), end=' ')
print()