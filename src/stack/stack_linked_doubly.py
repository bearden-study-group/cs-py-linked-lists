from src.linked_lists.doubly_linked_list.doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_tail()
