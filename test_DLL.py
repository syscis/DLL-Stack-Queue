import unittest
from DoublyLinkedList import DoublyLinkedList

__author__ = 'Hunt Blanchat'


class TestDeveloper(unittest.TestCase):

    def setUp(self):
        self.dub_list = DoublyLinkedList()
        self.dub_list.add_front(1)
        self.dub_list.add_rear(10)
        self.dub_list.add_rear(11)
        self.dub_list1 = DoublyLinkedList()

    def tearDown(self):
        pass

    def test_index_of(self):
        self.assertEqual(self.dub_list.index_of(1), 0)
        self.assertEqual(self.dub_list.index_of(10), 1)
        self.assertEqual(self.dub_list.index_of(11), 2)
        self.assertEqual(self.dub_list.index_of(100), -1)
        self.assertEqual(self.dub_list.index_of('Queequeg'), -1)
        self.assertEqual(self.dub_list1.index_of('Stubb'), -1)

    def test_insert_at(self):
        self.dub_list.insert_at(0, 1000)
        self.assertEqual(self.dub_list.at_index(0), 1000)
        self.assertEqual(self.dub_list.at_index(1), 1)
        self.assertEqual(self.dub_list.at_index(2), 10)
        self.assertEqual(self.dub_list.at_index(3), 11)
        self.dub_list.insert_at(3, 500)
        self.assertEqual(self.dub_list.at_index(3), 500)
        self.assertEqual(self.dub_list.size, 5)

        self.dub_list1.insert_at(-1, 'NA')
        self.assertEqual(self.dub_list1.at_index(0), 'NA')
        self.dub_list1.insert_at(0, 'Fa, La!')
        self.dub_list1.insert_at(-1, 'Lirra, Skirra!')
        self.assertEqual(self.dub_list1.remove_at(-1), 'NA')
        self.dub_list1.insert_at(-1, 'Great')
        self.dub_list1.insert_at(-2, 'Verily')
        self.dub_list1.insert_at(-4, 'Oi')
        self.dub_list1.print_it_out()
        self.dub_list1.print_in_reverse()
        self.assertRaises(IndexError, lambda: self.dub_list1.insert_at(-9999, 'never!'))

    def test_remove_at(self):
        self.assertEqual(self.dub_list.remove_at(0), 1)
        self.assertEqual(self.dub_list.size, 2)
        self.assertEqual(self.dub_list.remove_at(1), 11)
        self.assertEqual(self.dub_list.size, 1)
        self.assertEqual(self.dub_list.remove_at(0), 10)
        self.dub_list.insert_at(0, 'hat')
        self.dub_list.insert_at(-1, 'cat')
        self.assertEqual(self.dub_list.remove_at(0), 'cat')
        self.assertEqual(self.dub_list.remove_at(1), 'hat')
        self.assertEqual(self.dub_list.size, 0)
        self.assertRaises(IndexError, lambda: self.dub_list.remove_at(0))


if __name__ == '__main__':
    unittest.main()