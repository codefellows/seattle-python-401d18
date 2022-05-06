class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        Traverse the tree in a pre-order fashion
        return list of the values in correct order
        """

        def walk(root, values):  # root = a Node or none. Recursive function

            # every recursive function needs to know when to stop, aka base case
            if not root:
                return

            # Task 1: do something
            values.append(root.value)

            # Task 2: go left
            walk(root.left, values)

            # Task 3: go right
            walk(root.right, values)

        ordered_values = []

        walk(self.root, ordered_values)

        return ordered_values

    def in_order(self):
        """
        Traverse the tree in an i-order fashion
        return list of the values in correct order
        """

        def walk(root, values):  # root = a Node or none. Recursive function

            # every recursive function needs to know when to stop, aka base case
            if not root:
                return

            # Task 1: go left
            walk(root.left, values)

            # Task 2: do something
            values.append(root.value)

            # Task 3: go right
            walk(root.right, values)

        ordered_values = []

        walk(self.root, ordered_values)

        return ordered_values

    def post_order(self):
        """
        Traverse the tree in a post-order fashion
        return list of the values in correct order
        """

        def walk(root, values):  # root = a Node or none. Recursive function

            # every recursive function needs to know when to stop, aka base case
            if not root:
                return

            # Task 1: go left
            walk(root.left, values)

            # Task 2: go right
            walk(root.right, values)

            # Task 3: do something
            values.append(root.value)

        ordered_values = []

        walk(self.root, ordered_values)

        return ordered_values
