# Queue: A queue.
# Your implementation should pass the tests in test_queue.py.
# LAURYN GOMEZ

from pyllist import sllist

class Queue:
    def __init__(self):
        self.data = sllist()

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.popleft()