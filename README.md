# cs-py-linked-lists

 This folder is a collection of implementations of LinkedLists, Stacks, and Queues.

## Linked List Overview

A linked list is a simple, linear data structure used to store a collection of elements. Unlike an array (or list in
Python), each element in a LinkedList does not have to be stored contiguously in memory.

For example, in an array, each element of the list `[43, 32, 63]` is stored like so:

![Diagram of Array (or Python List)](https://tk-assets.lambdaschool.com/61d549f9-9f66-4d1f-9572-2d43098c2767_arrays-stored-in-memory.001.jpeg)

`43` is the first item in the collection and is therefore stored in the first slot. `32` is the second item and is
stored immediately next to `43` in memory.

In a *LinkedList*, each element of the list could be stored like so:

![Diagram of LinkedList in Memory](https://tk-assets.lambdaschool.com/72151497-7a5e-4940-835c-d8beb9c88922_linked-list-in-memory.001.jpeg)

You can see here that the elements can be spaced out in memory. Because the elements are not stored contiguously, each
element in memory must contain information about the next item in the list! The first item stores the data `43`  as well
as the location in memory `*3` for the next item in the list. This example is simplified; the second item in the
list (`32`) could be located ANYWHERE in memory.

## Time & Space Complexity

### Lookup

To look up an item by its index in a linked list is linear time`O(n)`. To traverse THROUGH a linked list, you first have
to start with the head reference to the node and then follow each subsequent pointer to the next item in the chain.

### Append

Adding an item to a Linked List is constant time `O(1)`. We always have a reference point to the tail of the linked
list, so we can easily insert an item after the tail.

### Insert

In the worst case, inserting an item in a linked list is LINEAR time `O(n)`. To insert an item at a specific index, we
have to traverse FROM THE BEGINNING until the DESIRED index.

### Delete

In the worst case, deleting an item in a linked list is linear time `O(n)`. Just like insertion, deleting an item at a
specific index means traversing the list starting at the head.

### Space

The space complexity of a linked list is linear time `O(n)`. Each item in the linked list will take up space in memory.

### Strengths of LinkedList

The primary strength of a linked list is that operations on the linked list's ends are FAST. This is b/c the linked list
always has a reference to teh head (first node) and tail (last node) of the list. Doing ANYTHING on the ends is CONSTANT
TIME!! Regardless of how many items are in the list!! This is why Heaps and Queues use a linked-list implementation all
the time. Only operating on ends.

Additionally, just like a dynamic array, you don't have to set a capacity to a linked list when you instantiate it. If
you don't know the size of the data you are storing, or if the amount of data is likely to fluctuate, linked lists can
work well.

### Weaknesses of a Linked List

The main weakness of a linked list is not efficiently accessing an "index" in the middle of the list. The only way that
the linked list can get to the seventh item in the linked ist is by going to the head node and then traversing one node
at a time until you arrive at the seventh node. 


## Various Implementations
### Singly Linked List
### Doubly Linked List
### Queue
### Stack
### XOR Linked List (Coming Soon)
### Circular Linked List (Coming Soon)
