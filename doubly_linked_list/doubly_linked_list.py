from typing import Optional


class Node:
    """
    Each Node holds a reference to its previous node
    as well as its next_node node in the List. That two-directional
    reference is what allows for our DoublyLinkedList to be
    doubly-linked!
    """

    def __init__(self,
                 value,  # required, could be of any type
                 prev: Optional["Node"] = None,  # optional, instance of Node or None
                 next_node: Optional["Node"] = None  # optional, instance of Node or None
                 ):
        """
        Constructs a Node instance that stores the specified value

        :param value: The value to store
        :param prev: a reference to the previous node (defaults to None)
        :param next_node: a reference to the next node (defaults to None)
        """

        self.value = value  # the value to store
        self.prev = prev  # the node before this one — defaults to None
        self.next = next_node  # the node after this one — defaults to None

    def __repr__(self):
        return f"Node({self.value})"


class DoublyLinkedList:
    """
    A class implementation of a Doubly-Linked-List

    It holds references to the list's head and tail nodes as well as the list's size
    """

    def __init__(self, node_list: Optional[list] = None):
        """
        Constructs an instance of DoublyLinkedList class.

        :param node_list: an optional list of values to to initialize the DoublyLinkedList with.
        If no list is given, our DLL will start as empty
        """
        self.head = self.tail = None  # initialize head and tail to None
        self.size = 0  # number of items stored in DLL

        # if given node_list exists
        if node_list is not None:
            # then add each value in list to tail
            for value in node_list:
                self.add_to_tail(value)

    def __repr__(self):
        """Returns a string representation of this DoublyLinkedList"""

        str_repr = "DLL=["

        if self.size == 0:  # if no items in list
            return f"{str_repr}]"

        current_node = self.head  # start at head

        while current_node is not None:
            str_repr += f"{current_node}{']' if current_node is self.tail else ' -> '}"
            current_node = current_node.next

        return str_repr

    def __len__(self):
        """returns the number of nodes stored in list"""

        return self.size

    def add_to_head(self, value):
        """inserts a Node with the given value as the new head of the list"""

        # Wraps the given value in a Node and inserts it
        # as the new head of the list.
        #
        # Don't forget to handle the old head node's previous pointer accordingly.

        new_node = Node(value)

        # if no items in list
        if self.size == 0:
            # new_node will be the only element,
            # therefore it will be both the head and the tail!
            self.head = self.tail = new_node

        # else, there is at least one item in list
        else:
            # assign current head as new_node's .next reference
            new_node.next = self.head
            # assign current head's previous pointer as new_node (instead of None)
            self.head.prev = new_node
            # assign new_node as the new head!
            self.head = new_node

        # increments the size attribute after adding node to list
        self.size += 1

    def remove_head(self):
        """
        Removes the node at the head of the list

        Removes the node at the head of the list, making the
        current head's next node the new head of the List.

        Returns the value of the removed Node.
        """

        # if there are no elements in list
        if self.size == 0:
            # nothing to remove (and nothing to return)
            return None

        # make a copy of the node to be deleted
        removed_value = self.head.value

        # if only one element in list
        if self.size == 1:
            # then assign head and tail to None, effectively
            # removing the previously stored element
            self.head = self.tail = None

        # else, there is more than one element in list (at least two nodes)
        else:
            # shift head right (reassign head to head.next_node)
            self.head = self.head.next
            # reassign head.prev to point at None (it used to point at old_head)
            self.head.prev = None

        self.size -= 1
        return removed_value

    def add_to_tail(self, value):
        """wraps the given value in a Node and inserts it as the new tail of the list"""

        new_node = Node(value)

        if self.size == 0:  # if list is empty
            # make new_node both head and tail
            # (as it is the only element in list!)
            self.head = self.tail = new_node

        else:  # list has at LEAST one element
            self.tail.next = new_node  # place new_node after tail
            new_node.prev = self.tail  # place current tail before new_node
            self.tail = new_node  # replace self.tail

        self.size += 1  # increase size of list

    def remove_tail(self):
        """Returns the value of the removed Node."""

        # Removes the List's current tail node, making the
        # current tail's previous node the new tail of the List.

        if self.size == 0:  # if list is empty
            return None  # nothing to remove; return out

        tail_to_remove = self.tail  # copy value of current tail before deletion (for return)

        if self.size == 1:  # if only one item in list
            self.head = self.tail = None  # list will now be empty

        else:
            self.tail.prev.next = None  # reassign new tail's prev to None (last item)
            self.tail = self.tail.prev  # shift tail left

        tail_to_remove.prev = tail_to_remove.next = None  # remove any ties to list
        self.size -= 1  # decrease size (deleting el)
        return tail_to_remove.value  # return value of removed tail

    def move_to_front(self, node):
        """Relocates given node from its current location to front of list"""

        if self.size == 0:  # no items in list
            return None  # nothing to move; return out

        if self.head is node:  # if node is head already
            return None  # nothing to move, node is at beginning; return out

        if self.tail is node:  # if node is tail
            self.tail = node.prev  # shift tail left

        else:  # else node must not be tail
            # if node is not tail, then node.next_node is not None
            node.next.prev = node.prev  # sew node.next_node to node.prev

        node.prev.next = node.next  # if node=tail next_node is None; else, next_node is a node. Works either way!
        self.head.prev = node  # assign current head's prev to point at node instead of None
        node.next = self.head  # place node before head
        node.prev = None  # reassign node.prev to point at None (no nodes before head and node is about to be head)
        self.head = node  # reassign head (shifting left) head is now node

    def move_to_end(self, node):
        """Relocates given node from its current location to end of list"""

        if self.size == 0:  # no items in list
            return None  # no such node (nothing to move)

        if node is self.tail:  # node is already at end as it is the tail
            return None  # node does not need to be moved

        if node is not self.head:
            # node must be in the middle of list (node is neither head nor tail, list is not empty)
            node.prev.next = node.next  # since node is not head, deal with node.prev

        else:  # if node is at the beginning of the list
            self.head = node.next

        node.next.prev = node.prev  # assign the next_node's prev pointer to point at prev_node
        self.tail.next = node  # point current_tail.next_node at node
        node.prev = self.tail  # point node.prev at current_tail
        node.next = None  # assign node.next_node none as it will be tail (and thus at end of list)
        self.tail = node  # assign node as tail

    def delete(self, node):
        """Deletes the given node from the list, preserving the order of the other elements of the List.
        """

        if self.size == 0:  # if list is empty
            return None  # nothing to delete

        removed_value = node.value  # copy deleted node's value

        if self.size == 1:  # if only one item in list
            self.head = self.tail = None

        else:  # more than one element in list
            if self.head is node:  # node to delete is head
                self.head = node.next  # reassign head to be element after head

            elif self.tail is node:  # node to delete is tail
                self.tail = node.prev  # reassign tail to be element before tail

            else:  # node is neither head nor tail, putting it somewhere in the middle
                node.prev.next = node.next
                node.next.prev = node.prev

            node.next = node.prev = None

        self.size -= 1
        return removed_value

    def get_max(self):
        """finds and returns the maximum value of all the nodes in the list."""

        max_value = self.head.value
        current_node = self.head.next
        # while current_node.next_node is not None: # when current_node = current.tail, this will not iterate
        while current_node is not None:  # when current_node = current.tail, this will not iterate
            # checks if the value is larger than our max value so far
            if max_value < current_node.value:
                max_value = current_node.value

            current_node = current_node.next

        return max_value
