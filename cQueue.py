import DoublyLinkedList

__author__ = 'Hunt Blanchat'


class Queue:

    def __init__(self):
        """
        Creates an object of Doubly Linked List and stores it in the variable queue
        to be used as a Queue Data Structure
        """
        self.queue = DoublyLinkedList.DoublyLinkedList()

    def is_empty(self):
        """ Checks if the Doubly Linked List is empty or the Queue

        :return: Bool
        """
        return self.queue.size == 0

    def size(self):
        """ Checks the size of the Doubly Linked List or the Queue

        :return: int
        """
        return self.queue.size

    def enqueue(self, value):
        """ Adds an item to the Doubly Linked List or the Queue

        :param value: item being stored in Doubly Linked List
        :return: None
        """
        self.queue.add_rear(value)

    def dequeue(self):
        """ Removes an item from the front of the list or Queue and returns that value

        :return: value stored in removed Node
        """
        return self.queue.remove_front()


def main():
    quack = Queue()
    print(quack.is_empty())
    print(quack.size())
    quack.enqueue('cat')
    print(quack.dequeue())


if __name__ == '__main__':
    main()