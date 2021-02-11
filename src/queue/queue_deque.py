"""
This is a quick and dirty implementation of a queue.
If you're coding on the GCA, my personal recommendation for
implementing a queue would look like this.
"""
from collections import deque


class Queue:
    def __init__(self):
        self.storage = deque()

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.appendleft(value)  # add to head

    def dequeue(self):
        if len(self.storage) == 0:
            return None  # nothing to _remove, nothing to return

        return self.storage.pop()  # _remove from tail


# or, more likely, you'll have some problem to solve that will use a queue
def use_queue():
    q = deque()
    print(f"Queue on construction: {q}")
    q.append("a")
    q.append("b")
    q.append("c")
    print(f"Queue after ABC: {q}")

    while len(q) > 0:
        print(f"popped item: {q.popleft()}")

    print(f"Queue after removing all elements: {q}")


# use_queue()
