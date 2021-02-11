class Stack:
    def __init__(self):
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        # if self.storage list is empty
        if len(self.storage) == 0:
            # then return out, the pop() below would throw an error
            return

        return self.storage.pop()
