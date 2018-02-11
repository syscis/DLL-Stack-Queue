import unittest
import cStack
from DoublyLinkedList import DoublyLinkedList


class TestDeveloper(unittest.TestCase):  # inherits numerous assert methods
    # order of testing is not sequential
    def setUp(self):  # allows initialization of data prior to each test
        self.stack_1 = cStack.Stack()

    def tearDown(self):  # allows tear down of setUp prior to each test
        pass

    def test_has_a_dll(self):  # always begin test method names with test_
        self.assertIsInstance(self.stack_1.stack, DoublyLinkedList, 'Stack must be built using DLL')

    def test_no_list(self):
        self.assertNotIsInstance(self.stack_1.stack, list, 'Stack should not be built using []')

    def test_author(self):
        try:
            print(cStack.__author__)
        except AttributeError as ae:
            print(ae)

    def test_is_empty(self):
        self.assertTrue(self.stack_1.is_empty())
        self.assertEqual(self.stack_1.size(), 0)

    def test_push(self):
        self.assertIsNone(self.stack_1.push('turtle'), 'Push returns None')
        self.stack_1.push(44)
        self.assertEqual(self.stack_1.size(), 2)

    def test_pop(self):
        self.stack_1.push('turtle')
        self.stack_1.push(44)
        self.assertEqual(self.stack_1.pop(), 44)
        self.assertEqual(self.stack_1.pop(), 'turtle')

    def test_peek(self):
        self.stack_1.push('turtle')
        self.stack_1.push(44)
        size = self.stack_1.size()
        self.assertEqual(self.stack_1.peek(), 44)
        self.assertEqual(self.stack_1.size(), size)


if __name__ == '__main__':
    unittest.main()