from src.linked_lists.singly_linked_list.singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        removed_item = self.storage.remove_tail()
        if removed_item is not None:
            self.size -= 1

        return removed_item
