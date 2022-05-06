from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):

    def add(self, value):

        def walk(root, new_node):

            # base case
            if not root:
                return

            if new_node.value < root.value:
                # go left
                if root.left:
                    walk(root.left, new_node)
                else:
                    root.left = new_node
            else:
                # go right
                if root.right:
                    walk(root.right, new_node)
                else:
                    root.right = new_node

        node_to_add = Node(value)

        if not self.root:
            self.root = node_to_add
            return

        walk(self.root, node_to_add)
