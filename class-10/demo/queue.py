from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.rear = None
        self.front = None

    def enqueue(self, value):
        node = Node(value)

        if self.rear:
            self.rear.next = node

        self.rear = node

        if not self.front:
            self.front = self.rear

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError

        old_front = self.front
        self.front = old_front.next

        return old_front.value

    def peek(self):

        if not self.front:
            raise InvalidOperationError

        return self.front.value

    def is_empty(self):
        return not self.front
