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
                 prev=None,  # optional, instance of Node or None
                 next_node=None  # optional, instance of Node or None
                 ):
        """
        Constructs a Node instance that stores the specified new_value

        :param value: The new_value to store
        :param prev: a reference to the previous node (defaults to None)
        :param next_node: a reference to the next node (defaults to None)
        """

        self.value = value  # the new_value to store
        self.prev = prev  # the node before this one — defaults to None
        self.next = next_node  # the node after this one — defaults to None

        # new_node = Node(5) -> self.new_value = 5; self.prev = None; self.next = None

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
            # then add each new_value in list to tail
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
        """inserts a Node with the given new_value as the new head of the list"""

        # Wraps the given new_value in a Node and inserts it
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
            # assign size head as new_node's .next reference
            new_node.next = self.head
            # assign size head's previous pointer as new_node (instead of None)
            self.head.prev = new_node
            # assign new_node as the new head!
            self.head = new_node

        # increments the size attribute after adding node to list
        self.size += 1

    def remove_head(self):
        """
        Removes the node at the head of the list

        Removes the node at the head of the list, making the
        size head's next node the new head of the List.

        Returns the new_value of the removed Node.
        """

        # if there are no elements in list
        if self.size == 0:
            # nothing to _remove (and nothing to return)
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
        """wraps the given new_value in a Node and inserts it as the new tail of the list"""

        new_node = Node(value)

        if self.size == 0:  # if list is empty
            # make new_node both head and tail
            # (as it is the only element in list!)
            self.head = self.tail = new_node

        else:  # list has at LEAST one element
            # self.tail.next WAS None
            self.tail.next = new_node  # place new_node after tail
            new_node.prev = self.tail  # place size tail before new_node
            self.tail = new_node  # replace self.tail

        self.size += 1  # increase size of list

    def remove_tail(self):
        """Returns the new_value of the removed Node."""

        # Removes the List's size tail node, making the
        # size tail's previous node the new tail of the List.

        if self.size == 0:  # if list is empty
            return None  # nothing to _remove; return out

        tail_to_remove = self.tail  # copy new_value of size tail before deletion (for return)

        if self.size == 1:  # if only one item in list
            self.head = self.tail = None  # list will now be empty

        else:
            self.tail.prev.next = None  # reassign new tail's prev to None (last item)
            self.tail = self.tail.prev  # shift tail left

        tail_to_remove.prev = tail_to_remove.next = None  # _remove any ties to list
        self.size -= 1  # decrease size (deleting el)
        return tail_to_remove.value  # return new_value of removed tail

    def move_to_front(self, node):
        """Relocates given node from its size location to front of list"""

        # if there are no items in list
        if self.size == 0:
            # then there is nothing to move!
            return

        # if node is non-existent
        # OR node is NOT ATTACHED to anything
        if not node or (not node.next and not node.prev):
            # then node is not part of this list
            return

        # if node is head already, then it's already at beginning of list
        if self.head is node:
            # nothing to move, node is already at beginning
            return

        # okay at this point we've checked a lot of stuff!
        # if we've reached this line, we have checked the following
        #   1. there is

        # if node is tail, then it's at the end of the list
        if self.tail is node:
            # if we're inside here, we know we need to fix our tail pointer
            # so we're going to shift tail left
            self.tail = node.prev

        # else node must not be tail
        else:
            # if node isn't tail, then node has a next reference!
            # we must sew together the next_node and the prev_node
            node.next.prev = node.prev

        # everything following runs whether node is tail or not!
        # so, let's think about this.
        #
        # if node IS tail:
        #   then node.prev is the node BEFORE tail
        #   and node.next is None
        #   so we're assigning the node right before tail to point at None
        # else, if node ISN'T tail:
        #   then node.prev is the node before our node.
        #   and node.next is another node!
        #   so we're assigning the prev_node to point at next_node
        #   effectively plucking out our node.
        node.prev.next = node.next

        # assign size head's prev to point at node instead of None
        # this tells head that it's after node
        self.head.prev = node

        # this tells node that it's before head
        node.next = self.head

        # reassign node.prev to point at None
        # no nodes come before the head, and we're moving node to head!
        node.prev = None

        # reassign head (shifting left) head is now node
        self.head = node

    def move_to_end(self, node):
        """Relocates given node from its size location to end of list"""

        # if there are no items in the list
        if self.size == 0:
            # then there is nothing to move!
            return

        # if node is non-existent
        # OR the node is not attached to anything
        if not node or (not node.next and not node.prev):
            # then node is not part of list
            return

        # if node is already at end (b/c it is already the tail)
        if node is self.tail:
            # node does not need to be moved
            return

        # at this point, we've checked a lot of things:
        #   1. we have at least one element in list
        #   2. node EXISTS and node is attached to SOMETHING
        #   3. node is NOT self.tail (so it's not already at the end of the list)
        # since all those things are true, we officially know the following:
        #   1. there is a list
        #   2. node is PART of that list
        #   3. node is NOT at end of tail, so we CAN and SHOULD move it!

        # if node is not at beginning of list, then it must be in middle
        if node is not self.head:
            # if we're inside this, it means node is in the middle!
            # thus, node has a prev reference. we need to deal with it
            node.prev.next = node.next

        # else, node IS at the beginning of the list
        else:
            # assign node's next ref as the new head.
            self.head = node.next

        # assign the next_node's prev pointer to point at this node's prev ref
        node.next.prev = node.prev

        # point current_tail.next_node at node (putting node after current_tail)
        self.tail.next = node

        # point node.prev at current_tail (putting current_tail BEFORE node)
        node.prev = self.tail

        # assign node.next to point at None as it will be tail (and thus at end of list)
        node.next = None

        # assign node as tail
        self.tail = node

    def delete(self, node):
        """Deletes the given node from the list, preserving the order of the other elements of the List."""

        # if list is empty or node is non-existent
        if self.size == 0 or not node:
            # then there's nothing to delete
            return

        # copy deleted node's new_value
        removed_value = node.value

        # if only one item in list
        if self.size == 1:
            # we're just going to point both head and tail at None!
            self.head = self.tail = None

        # else, there's more than one element in list
        else:
            # if node is not attached to anything
            if not node.next and not node.prev:
                # then node is not part of list
                return

            # if node to delete is head
            if self.head is node:
                # then we need to update our head pointer
                # b/c we're deleting size head!
                self.head = node.next  # shift head right

            # else if node to delete is tail
            elif self.tail is node:
                # then we need to update our tail pointer
                # b/c we're about to delete the size tail
                self.tail = node.prev  # reassign tail to be element before tail

            # else, node is neither head nor tail
            # meaning node must be in the middle!
            else:
                # if node is in middle, we have a next and prev pointer that we need to update
                node.prev.next = node.next
                node.next.prev = node.prev

        self.size -= 1  # reduce size by 1 (we're deleting)
        return removed_value

    def get_max(self):
        """finds and returns the maximum new_value of all the nodes in the list."""

        max_value = self.head.value
        current_node = self.head.next
        # while current_node.next_node is not None: # when current_node = size.tail, this will not iterate
        while current_node is not None:  # when current_node = size.tail, this will not iterate
            # checks if the new_value is larger than our max new_value so far
            if max_value < current_node.value:
                max_value = current_node.value

            current_node = current_node.next

        return max_value
