from pythonds import Queue
import matplotlib.pyplot as plt
import cQueue
import time
import numpy as np

__author__ = 'Hunt Blanchat'

def plot_queue_data(filename='QueueComparisonData.csv'):
    with open(filename, 'r') as file:
        file_data = file.readlines()

    n, my_enq, py_enq, my_deq, py_deq = np.loadtxt(file_data[1:], delimiter=',', unpack=True)
    plt.title('DLL Queue vs Py List Queue')
    plt.plot(n, my_enq, label='dll enqueue')
    plt.plot(n, py_enq, label='py enqueue')
    plt.plot(n, my_deq, label='dll dequeue')
    plt.plot(n, py_deq, label='py dequeue')

    plt.xlabel('N')
    plt.ylabel('Time (sec)')
    plt.legend()
    plt.show()


def get_words(file):
    """Retrieves lines from a text file, appends them to a list and returns said list

    :param file: file name in string format
    :return: list of lines in text file
    """
    dict_words = []
    for line in open(file, 'r'):
        line = line.strip()
        dict_words.append(line)
    print('Completed reading in {:,d} words to list'.format(len(dict_words)))
    return dict_words


def main():
    words = get_words('dictionary.txt')
    my_queue = cQueue.Queue()
    py_queue = Queue()
    out_file = open('QueueComparisonData.csv', 'w')
    out_file.write('N,dll enq,pyds enq,dll deq,pyds deq\n')
    print('\tN\t\tdll enq\t\tpyds enq\tdll deq\t\tpyds deq')
    for x in range(20000, 181000, 20000):
        my_enqueue_start = time.time()
        for y in range(x):
            my_queue.enqueue(words[y])
        my_enqueue_time = time.time() - my_enqueue_start

        py_enqueue_start = time.time()
        for y in range(x):
            py_queue.enqueue(words[y])
        py_enqueue_time = time.time() - py_enqueue_start

        my_dequeue_start = time.time()
        for y in range(x):
            my_queue.dequeue()
        my_dequeue_time = time.time() - my_dequeue_start

        py_dequeue_start = time.time()
        for y in range(x):
            py_queue.dequeue()
        py_dequeue_time = time.time() - py_dequeue_start
        print('{:,d}\t\t{:.3G}\t\t{:.3G}\t\t{:.3G}\t\t{:.3G}'.format(x, my_enqueue_time,
                                                                     py_enqueue_time, my_dequeue_time, py_dequeue_time))
        out_file.write('{:d},{:.3G},{:.3G},{:.3G},{:.3G}\n'.format(x, my_enqueue_time,
                                                                    py_enqueue_time, my_dequeue_time, py_dequeue_time))
    out_file.close()
    plot_queue_data()


if __name__ == '__main__':
    main()