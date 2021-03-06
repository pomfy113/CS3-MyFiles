#!python

from binarytree import BinarySearchTree, BinaryTreeNode
import unittest


class BinaryTreeNodeTest(unittest.TestCase):

    def test_init(self):
        data = 123
        node = BinaryTreeNode(data)
        assert node.data is data
        assert node.left is None
        assert node.right is None

    def test_is_leaf(self):
        # Create node with no children
        node = BinaryTreeNode(2)
        assert node.is_leaf() is True
        # Attach left child node
        node.left = BinaryTreeNode(1)
        assert node.is_leaf() is False
        # Attach right child node
        node.right = BinaryTreeNode(3)
        assert node.is_leaf() is False
        # Detach left child node
        node.left = None
        assert node.is_leaf() is False
        # Detach right child node
        node.right = None
        assert node.is_leaf() is True

    def test_is_branch(self):
        # Create node with no children
        node = BinaryTreeNode(2)
        assert node.is_branch() is False
        # Attach left child node
        node.left = BinaryTreeNode(1)
        assert node.is_branch() is True
        # Attach right child node
        node.right = BinaryTreeNode(3)
        assert node.is_branch() is True
        # Detach left child node
        node.left = None
        assert node.is_branch() is True
        # Detach right child node
        node.right = None
        assert node.is_branch() is False


class BinarySearchTreeTest(unittest.TestCase):

    def test_init(self):
        tree = BinarySearchTree()
        assert tree.root is None
        assert tree.size == 0
        assert tree.is_empty() is True

    def test_init_with_list(self):
        tree = BinarySearchTree([2, 1, 3])
        assert tree.root.data == 2
        assert tree.root.left.data == 1
        assert tree.root.right.data == 3
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_init_with_list_of_strings(self):
        tree = BinarySearchTree(['B', 'A', 'C'])
        assert tree.root.data == 'B'
        assert tree.root.left.data == 'A'
        assert tree.root.right.data == 'C'
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_init_with_list_of_tuples(self):
        tree = BinarySearchTree([(2, 'B'), (1, 'A'), (3, 'C')])
        assert tree.root.data == (2, 'B')
        assert tree.root.left.data == (1, 'A')
        assert tree.root.right.data == (3, 'C')
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_size(self):
        tree = BinarySearchTree()
        assert tree.size == 0
        tree.insert('B')
        assert tree.size == 1
        tree.insert('A')
        assert tree.size == 2
        tree.insert('C')
        assert tree.size == 3

    def test_search_with_3_items(self):
        # Create a complete binary search tree of 3 items in level-order
        items = [2, 1, 3]
        tree = BinarySearchTree(items)
        assert tree.search(1) == 1
        assert tree.search(2) == 2
        assert tree.search(3) == 3
        assert tree.search(4) is None

    def test_search_with_7_items(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        for item in items:
            assert tree.search(item) == item
        assert tree.search(8) is None

    def test_search_with_3_strings(self):
        # Create a complete binary search tree of 3 items in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        assert tree.search('A') == 'A'
        assert tree.search('B') == 'B'
        assert tree.search('C') == 'C'
        assert tree.search('D') is None

    def test_search_with_7_strings(self):
        # Create a complete binary search tree of 7 items in level-order
        items = ['D', 'B', 'F', 'A', 'C', 'E', 'G']
        tree = BinarySearchTree(items)
        for item in items:
            assert tree.search(item) == item
        assert tree.search('H') is None

    def test_insert_with_3_items(self):
        # Create a complete binary search tree of 3 items in level-order
        tree = BinarySearchTree()
        tree.insert(2)
        assert tree.root.data == 2
        assert tree.root.left is None
        assert tree.root.right is None
        tree.insert(1)
        assert tree.root.data == 2
        assert tree.root.left.data == 1
        assert tree.root.right is None
        tree.insert(3)
        assert tree.root.data == 2
        assert tree.root.left.data == 1
        assert tree.root.right.data == 3

    def test_insert_with_7_items(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree()
        for item in items:
            tree.insert(item)
        assert tree.root.data == 4
        assert tree.root.left.data == 2
        assert tree.root.right.data == 6
        assert tree.root.left.left.data == 1
        assert tree.root.left.right.data == 3
        assert tree.root.right.left.data == 5
        assert tree.root.right.right.data == 7

    # This space intentionally left blank (please do not delete this comment)

    def test_items_in_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        # Ensure the in-order traversal of tree items is ordered correctly
        assert tree.items_in_order() == ['A', 'B', 'C']

    def test_items_pre_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        # Ensure the pre-order traversal of tree items is ordered correctly
        assert tree.items_pre_order() == ['B', 'A', 'C']

    def test_items_post_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        # Ensure the post-order traversal of tree items is ordered correctly
        assert tree.items_post_order() == ['A', 'C', 'B']

    def test_items_level_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        # Ensure the level-order traversal of tree items is ordered correctly
        assert tree.items_level_order() == ['B', 'A', 'C']

    def test_items_in_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        # Ensure the in-order traversal of tree items is ordered correctly
        assert tree.items_in_order() == [1, 2, 3, 4, 5, 6, 7]

    def test_items_pre_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        # Ensure the pre-order traversal of tree items is ordered correctly
        assert tree.items_pre_order() == [4, 2, 1, 3, 6, 5, 7]

    def test_items_post_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        # Ensure the post-order traversal of tree items is ordered correctly
        assert tree.items_post_order() == [1, 3, 2, 5, 7, 6, 4]

    def test_items_level_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        # Ensure the level-order traversal of tree items is ordered correctly
        assert tree.items_level_order() == [4, 2, 6, 1, 3, 5, 7]

    def test_height_and_size(self):
        # Let's try for a balanced tree first
        items = BinarySearchTree([4])
        assert items.height() == 0
        assert items.size == 1
        # Height 1
        items.insert(2)  # Insert item, tree grows to 1
        assert items.height() == 1
        assert items.size == 2
        items.insert(6)  # Insert item 2; level is full, tree remains 1
        assert items.height() == 1
        assert items.size == 3
        # Height 2
        items.insert(1)
        assert items.height() == 2
        assert items.size == 4
        items.insert(3)
        assert items.height() == 2
        assert items.size == 5
        items.insert(5)
        assert items.height() == 2
        assert items.size == 6
        items.insert(7)
        assert items.height() == 2
        assert items.size == 7

        # Unbalanced tree
        items = BinarySearchTree([1, 2])
        assert items.height() == 1
        assert items.size == 2
        items.insert(3)
        assert items.height() == 2
        assert items.size == 3
        items.insert(4)
        assert items.height() == 3
        assert items.size == 4
        items.insert(6)
        assert items.height() == 4
        assert items.size == 5
        items.insert(7)
        assert items.height() == 5
        assert items.size == 6
        items.insert(5)  # Let's throw a left branching for good measure
        assert items.height() == 5
        assert items.size == 7

    def test_delete(self):
        items = [4, 2, 6, 1, 3, 5, 7]
        # Balanced tree
        tree = BinarySearchTree(items)
        assert tree.items_level_order() == [4, 2, 6, 1, 3, 5, 7]
        assert tree.size == 7
        # Delete leaves
        tree.delete(7)
        assert tree.items_level_order() == [4, 2, 6, 1, 3, 5]
        assert tree.size == 6
        tree.delete(1)
        assert tree.items_level_order() == [4, 2, 6, 3, 5]
        assert tree.size == 5
        # Delete nodes with one branch
        tree.delete(2)
        assert tree.items_level_order() == [4, 3, 6, 5]
        assert tree.size == 4
        tree.delete(6)
        assert tree.items_level_order() == [4, 3, 5]
        assert tree.size == 3

        # Reset
        tree = BinarySearchTree(items)
        assert tree.items_level_order() == [4, 2, 6, 1, 3, 5, 7]
        assert tree.size == 7
        # Delete double branch
        tree.delete(2)
        assert tree.items_level_order() == [4, 1, 6, 3, 5, 7]
        assert tree.size == 6
        tree.delete(6)
        assert tree.items_level_order() == [4, 1, 5, 3, 7]
        assert tree.size == 5

        # Reset
        tree = BinarySearchTree(items)
        assert tree.items_level_order() == [4, 2, 6, 1, 3, 5, 7]
        assert tree.size == 7
        # Delete root
        tree.delete(4)
        print(tree.items_level_order())
        assert tree.items_level_order() == [3, 2, 6, 1, 5, 7]

        # Larger tree
        items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        tree = BinarySearchTree(items)
        tree.delete(8)
        assert tree.items_level_order() == [7, 4, 12, 2, 6, 10, 14, 1, 3, 5, 9, 11, 13, 15]
        tree.delete(7)
        print(tree.items_level_order())
        assert tree.items_level_order() == [6, 4, 12, 2, 5, 10, 14, 1, 3, 9, 11, 13, 15]
        tree.delete(6)
        print(tree.items_level_order())
        assert tree.items_level_order() == [5, 4, 12, 2, 10, 14, 1, 3, 9, 11, 13, 15]

if __name__ == '__main__':
    unittest.main()
