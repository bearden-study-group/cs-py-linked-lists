class Queue:
    def __init__(self):
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.insert(0, value)  # add to head

    def dequeue(self):
        if not self.storage:
            return None  # nothing to _remove, nothing to return

        return self.storage.pop()  # _remove from tail
