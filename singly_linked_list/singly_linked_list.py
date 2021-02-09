class Node:
    """
    Class representation of a DoublyLinkedList Node.

    Each Node will store a value and a reference
    to the next_node Node in list.
    """

    def __init__(self, value=None):
        """
        Constructor for a Node instance

        :param value: the value to store within this node.
        Defaults to None if no value given
        """

        # the value to store in this Node (can be of any type)
        self.value = value

        # a reference to the next_node node (only None if Node is last in list)
        self.next = None

    def __repr__(self):
        """
        A string representation of any node instance.

         Used in place of __str__ if __str__ is not defined, otherwise
         used mostly internally.
        """

        return f"Node({repr(self.value)}"


class LinkedList:
    """
    A class representation of a singly-linked-list.

    Stores a reference to both the head (first node in list)
    and the tail (last node in list). Each item in list will be of
    class Node (defined above) and will store a value and a reference
    to the next_node Node in list.
    """

    def __init__(self):
        """
        Constructor method for a DoublyLinkedList instance
        """

        self.head = None
        self.tail = None

    def add_to_head(self, value):
        """
        Adds an item to the beginning of the list

        :param value: the value to store at the beginning of the list
        :return: None
        """

        # initialize a Node with the given value
        new_node = Node(value)

        # if there are no items in list
        if self.head is None:
            # then new_node will be only item in list
            # therefore it will be the head and tail!
            self.head = self.tail = new_node
            # self.tail = new_node
            return

        # else, there is at least one item in list
        #
        # the new_node will come before current head
        # thus, the new_node.next_node should point at current head
        new_node.next = self.head

        # assign new_node as the current head
        self.head = new_node

    def add_to_tail(self, value):
        """
        Adds an item to the end of the list
        :param value: the value to store at the end of the list
        :return: None
        """

        # initialize a Node with the value to store
        new_node = Node(value)

        # if there are no items in list
        if self.head is None:
            # then new_node will be only item in list
            # therefore it will be the head and tail!
            self.head = self.tail = new_node
            # self.tail = new_node
            return  # return out to end method

        # else, there is at least one item in list
        #
        # current tail should point to new_node, as new_node will
        # the element AFTER the current tail
        self.tail.next = new_node

        # assign new_node as the new tail
        self.tail = new_node

    def remove_head(self):
        """
        Remove the item at the beginning of the list
        :return: The value of the item being removed
        """

        # if there are no items in list
        if self.head is None:
            # then there is nothing to remove (and nothing to return)!
            return

        # make a copy of the old head value before we delete it
        old_head_value = self.head.value

        # if only one item in list
        if self.head.next is None:
            # then remove the tail's reference to our only Node
            # instead, point self.tail at None
            self.tail = None

        # most important part of method below
        # notice that this happens with one item in list or more
        #
        # assign our self.head to point at the next_node Node,
        # effectively removing self.head from the list entirely
        self.head = self.head.next

        # return the old head's value
        return old_head_value

    def remove_tail(self):
        """
        Remove the item at the end of the list
        :return: The value of the item being removed
        """

        # if zero items in the list
        if self.head is None:
            # then there's nothing to delete (or return)!
            return

        # copy the old tail's value before we delete it
        old_tail_value = self.tail.value

        # if only one item in list
        if self.head.next is None:
            # then we can assign head and tail to point at None!
            self.head = self.tail = None
            # return old value
            return old_tail_value

        # else, there are at least 2 nodes in list (or more)
        #
        # loop through entire list until we hit the Node BEFORE self.tail

        current_node = self.head  # start at very beginning
        # if current_node.next_node IS self.tail, then we have the node before tail!
        # otherwise, loop again
        while current_node.next is not self.tail:
            # reassign our current_node pointer to its next_node value
            current_node = current_node.next

        # reassign current_node.next_node to point at None rather
        # than the node that is at self.tail
        current_node.next = None
        # then, reassign current_node as the new tail!
        self.tail = current_node

        # return old tail's value
        return old_tail_value
