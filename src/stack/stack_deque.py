from collections import deque


class Stack:
    def __init__(self):
        self.storage = deque()

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        # if deque is empty,
        if len(self.storage) == 0:
            # then attempting to pop below would throw an error
            return

        return self.storage.pop()
