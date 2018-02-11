import unittest
import cQueue
from DoublyLinkedList import DoublyLinkedList


class TestDeveloper(unittest.TestCase):  # inherits numerous assert methods
    # order of testing is not sequential
    def setUp(self):  # allows initialization of data prior to each test
        self.queue_1 = cQueue.Queue()

    def tearDown(self):  # allows tear down of setUp prior to each test
        pass

    def test_has_a_dll(self):  # always begin test method names with test_
        self.assertIsInstance(self.queue_1.queue, DoublyLinkedList, 'Stack must be built using DLL')

    def test_no_list(self):
        self.assertNotIsInstance(self.queue_1.queue, list, 'Stack should not be built using []')

    def test_author(self):
        try:
            print(cQueue.__author__)
        except AttributeError as ae:
            print(ae)

    def test_is_empty(self):
        self.assertTrue(self.queue_1.is_empty())
        self.assertEqual(self.queue_1.size(), 0)

    def test_enqueue(self):
        self.assertIsNone(self.queue_1.enqueue('tortuga'), 'enqueue should return None')
        self.queue_1.enqueue(44)
        self.assertEqual(self.queue_1.size(), 2)

    def test_dequeue(self):
        self.queue_1.enqueue('turtle')
        self.queue_1.enqueue(44)
        self.queue_1.enqueue('tortuga')
        self.assertEqual(self.queue_1.dequeue(), 'turtle')
        self.assertEqual(self.queue_1.dequeue(), 44)

    def test_size(self):
        self.queue_1.enqueue('tortuga')
        self.queue_1.enqueue(44)
        size = self.queue_1.size()
        self.assertEqual(self.queue_1.size(), 2)
        self.assertEqual(self.queue_1.size(), size)


if __name__ == '__main__':
    unittest.main()