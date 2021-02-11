import unittest
from doubly_linked_list import DoublyLinkedList, Node


class DoublyLinkedListTests(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList([1])

    def test_set_up(self):
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 1)
        self.assertEqual(self.dll.size, 1)

    def test_empty_list_construction(self):
        new_dll = DoublyLinkedList([])
        self.assertIsNone(new_dll.head)
        self.assertIsNone(new_dll.tail)
        self.assertEqual(len(new_dll), 0)

    def test_repr(self):
        empty_dll = DoublyLinkedList()
        self.assertEqual(empty_dll.__repr__(), "DLL=[]")
        one_el_dll = DoublyLinkedList([1])
        self.assertEqual(one_el_dll.__repr__(), "DLL=[Node(1)]")
        long_dll = DoublyLinkedList([1, 2, 3, 4, 5, 6, 7])
        long_repr = "DLL=[Node(1) -> Node(2) -> Node(3) -> Node(4) -> Node(5) -> Node(6) -> Node(7)]"
        self.assertEqual(long_dll.__repr__(), long_repr)

    def test_default_construction(self):
        new_dll = DoublyLinkedList()
        self.assertIsNone(new_dll.head)
        self.assertIsNone(new_dll.tail)
        self.assertEqual(new_dll.size, 0)

    def test_list_construction(self):
        new_dll = DoublyLinkedList([1, 2, 3, 4, 5, 6])
        self.assertEqual(new_dll.head.value, 1)
        self.assertEqual(new_dll.tail.value, 6)
        self.assertEqual(new_dll.size, 6)

    def test_list_remove_from_tail(self):
        # test when list is empty
        empty_dll = DoublyLinkedList()
        self.assertIsNone(empty_dll.remove_tail())

        long_dll = DoublyLinkedList([1, 2, 3, 4])
        self.assertEqual(long_dll.remove_tail(), 4)
        self.assertEqual(len(long_dll), 3)

        self.dll.remove_tail()
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_tail(33)
        self.assertEqual(self.dll.head.value, 33)
        self.assertEqual(self.dll.tail.value, 33)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_tail(), 33)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_tail(68)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_tail(), 68)
        self.assertEqual(len(self.dll), 0)

    def test_list_remove_from_head(self):
        empty_dll = DoublyLinkedList()
        self.assertIsNone(empty_dll.remove_head())

        new_dll = DoublyLinkedList([1, 2, 3, 4])
        self.assertEqual(new_dll.remove_head(), 1)

        self.dll.remove_head()
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_head(2)
        self.assertEqual(self.dll.head.value, 2)
        self.assertEqual(self.dll.tail.value, 2)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_head(), 2)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_head(55)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_head(), 55)
        self.assertEqual(len(self.dll), 0)

    def test_list_add_to_tail(self):
        self.assertEqual(self.dll.tail.value, 1)
        self.assertEqual(len(self.dll), 1)

        self.dll.add_to_tail(30)
        self.assertEqual(self.dll.tail.prev.value, 1)
        self.assertEqual(self.dll.tail.value, 30)
        self.assertEqual(len(self.dll), 2)

        self.dll.add_to_tail(20)
        self.assertEqual(self.dll.tail.prev.value, 30)
        self.assertEqual(self.dll.tail.value, 20)
        self.assertEqual(len(self.dll), 3)

    def test_list_add_to_head(self):
        self.assertEqual(self.dll.head.value, 1)

        self.dll.add_to_head(10)
        self.assertEqual(self.dll.head.value, 10)
        self.assertEqual(self.dll.head.next.value, 1)
        self.assertEqual(len(self.dll), 2)

    def test_list_move_to_end(self):
        self.dll.add_to_head(40)
        self.assertEqual(self.dll.tail.value, 1)
        self.assertEqual(self.dll.head.value, 40)

        self.assertIsNone(self.dll.move_to_end(None))
        self.dll.move_to_end(self.dll.head)
        self.assertEqual(self.dll.tail.value, 40)
        self.assertEqual(self.dll.tail.prev.value, 1)
        self.assertEqual(len(self.dll), 2)

        self.dll.add_to_tail(4)
        self.dll.move_to_end(self.dll.head.next)
        self.assertEqual(self.dll.tail.value, 40)
        self.assertEqual(self.dll.tail.prev.value, 4)
        self.assertEqual(len(self.dll), 3)
        # test when node is tail
        self.assertIsNone(self.dll.move_to_end(self.dll.tail))
        # test when list is empty
        new_node = Node(10)
        new_dll = DoublyLinkedList()
        self.assertIsNone(new_dll.move_to_end(new_node))
        # test when node is not in list
        self.assertIsNone(self.dll.move_to_end(new_node))

    def test_list_move_to_front(self):
        unattached_node = Node(5)
        # test when list is empty
        empty_dll = DoublyLinkedList()
        self.assertIsNone(empty_dll.move_to_front(unattached_node))

        # test when Node is not in list
        long_dll = DoublyLinkedList([1, 2, 3, 4, 5, 6])
        # test when node is None
        self.assertIsNone(long_dll.move_to_front(None))
        # test when node is not in list
        self.assertIsNone(long_dll.move_to_front(unattached_node))
        # test when given node is head of list
        self.assertIsNone(long_dll.move_to_front(long_dll.head))

        self.dll.add_to_tail(3)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 3)

        self.dll.move_to_front(self.dll.tail)
        self.assertEqual(self.dll.head.value, 3)
        self.assertEqual(self.dll.head.next.value, 1)
        self.assertEqual(len(self.dll), 2)

        self.dll.add_to_head(29)
        self.dll.move_to_front(self.dll.head.next)
        self.assertEqual(self.dll.head.value, 3)
        self.assertEqual(self.dll.head.next.value, 29)
        self.assertEqual(len(self.dll), 3)

    def test_list_delete(self):
        # test delete when list is empty
        unattached_node = Node(5)
        empty_dll = DoublyLinkedList()
        self.assertIsNone(empty_dll.delete(unattached_node))

        long_dll = DoublyLinkedList([1, 2, 3, 4, 5, 6, 7])
        self.assertIsNone(long_dll.delete(unattached_node))
        # test delete where node is none
        self.assertIsNone(long_dll.delete(None))
        self.assertEqual(long_dll.delete(long_dll.tail), 7)
        self.assertEqual(long_dll.tail.value, 6)
        self.assertEqual(len(long_dll), 6)

        self.assertEqual(len(self.dll), 1)
        val_returned = self.dll.delete(self.dll.head)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_tail(1)
        self.dll.add_to_head(9)
        self.dll.add_to_tail(6)

        self.dll.delete(self.dll.head.next)
        self.assertEqual(self.dll.head.value, 9)
        self.assertEqual(self.dll.head.next, self.dll.tail)
        self.assertEqual(self.dll.tail.value, 6)

        self.dll.delete(self.dll.head)
        self.assertEqual(self.dll.head.value, 6)
        self.assertEqual(self.dll.tail.value, 6)
        self.assertEqual(len(self.dll), 1)

        self.dll.delete(self.dll.head)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

    def test_get_max_01(self):
        self.assertEqual(self.dll.get_max(), 1)
        self.dll.add_to_tail(100)
        self.assertEqual(self.dll.get_max(), 100)
        self.dll.add_to_tail(55)
        self.assertEqual(self.dll.get_max(), 100)
        self.dll.add_to_tail(101)
        self.assertEqual(self.dll.get_max(), 101)

    def test_get_max_at_head(self):
        new_dll = DoublyLinkedList([9, 1, 2, 3, 4, 5])
        self.assertEqual(new_dll.head.value, 9)
        self.assertEqual(new_dll.get_max(), 9)

    def test_get_max_at_tail(self):
        new_dll = DoublyLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(new_dll.tail.value, 9)
        self.assertEqual(new_dll.get_max(), 9)


if __name__ == '__main__':
    unittest.main()
