#!python

from queue import DeQueue

class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # TODO: Check if both left child and right child have no value
        if (self.left is None) and (self.right is None):
            return True
        else:
            return False

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        if (self.left is None) and (self.right is None):
            return False
        else:
            return True

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Runtime: Constant if 1 object, n due to looking at everything.
        """
        # Check if left child has a value and if so calculate its height
        left_height = right_height = 0
        if self.is_leaf():
            return 0
        if self.left is not None:
            node = self.left
            left_height = node.height() + 1
        # Check if right child has a value and if so calculate its height
        if self.right is not None:
            node = self.right
            right_height = node.height() + 1
        # Return one more than the greater of the left height and right height
        return max(right_height, left_height)

class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        n; going to go through everything"""
        # TODO: Check if root node has a value and if so calculate its height
        return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        log(n): it's going to traverse based on height, which is log(n) """
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        log(n): it's going to traverse based on height, which is log(n)"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return the node's data if found, or None
        return node.data if node else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        If it's empty, well, it's 1
        Otherwise, log(n); we know where we're heading"""
        # Handle the case where the tree is empty
        if self.is_empty():
            # Create a new root node
            self.root = BinaryTreeNode(item)
            # Increase the tree size
            self.size += 1
            return
        # Grab parent of where node should be
        parent = self._find_parent_node(item)
        # Check if the given item should be inserted left of parent node
        if item < parent.data:
            parent.left = BinaryTreeNode(item)
        # Check if the given item should be inserted right of parent node
        elif item > parent.data:
            parent.right = BinaryTreeNode(item)

        self.size += 1

    # def delete(self, item):
    #     """Oh man, this is a doozy."""
    #     if self.root.data == item:
    #         self.root = None
    #         self.size = 0
    #         print("Uprooted.")
    #
    #     parent = self._find_parent_node(item)
    #
    #     if parent is None:
    #         return
    #     elif parent.left.data is item:
    #         deletednode = parent.left
    #         if deletednode.is_leaf():
    #             deletednode = None
    #         elif parent.left.is_branch():
    #             parent.left = deletednode.right
    #             parent.left.left = deletednode.left
    #     elif parent.right.data is item:
    #         deletednode = parent.right
    #         if deletednode.is_leaf():
    #             deletednode = None
    #         elif parent.right.is_branch():
    #             parent.right = deletednode.right
    #             parent.right.left = deletednode.left
    #     self.size -= 1
    #     return
    def _find_node(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found.
        O(log(n)); the find_node goes through a certain series, so we only
        need to go a certain distance."""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Descend to the node's left child
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_parent_node(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Also log(n); we traverse height"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                # TODO: Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                # TODO: Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    # This space intentionally left blank (please do not delete this comment)

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            items = self._traverse_in_order_iterative(self.root, items)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_in_order_recursive(node.left, visit)
        # Visit this node's data with given function
        visit.append(node.data)
        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_in_order_recursive(node.right, visit)

        return visit


    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""

        queue = DeQueue()
        queue.enqueue_front(node)
        # I'm going to need a blackboard for this
        while queue.length() > 0:
            # Go as left as possible!
            while node.left is not None:
                queue.enqueue_front(node.left)
                node = node.left
            # If there's no more left, let's pop something + append
            else:
                node = queue.dequeue_front()
                visit.append(node.data)
                # Check right and eventually see if it has lefts
                # If it doesn't have a left, we skip the above while loop
                if node.right:
                    queue.enqueue_front(node.right)
                    node = node.right
        return visit



    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            items = self._traverse_pre_order_iterative(self.root, items)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # Visit this node's data with given function
        visit.append(node.data)
        # TODO: Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_pre_order_recursive(node.left, visit)
        # TODO: Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_pre_order_recursive(node.right, visit)

        return visit

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)
        # [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]
        queue = DeQueue()
        queue.enqueue_front(node)
        # I'm going to need a blackboard for this
        # while queue.length() > 0:
        #     while node.left is not None:
        #         queue.enqueue_front(node)
        #         node = node.left
        #         visit.append(node.data)
        #     else:
        #         node = queue.dequeue_front()
        #         if node.right:
        #             node = node.right
        #             visit.append(node.data)
        #
        # Above was close, but kept printing the root's right at the end!

        while queue.length() > 0:
            # Keep popping the first thing that shows up!
            node = queue.dequeue_front()
            visit.append(node.data)
            # We need to make sure we add the right first before left
            # This is to make sure the leftmost is stacked/printed last
            if node.right:
                queue.enqueue_front(node.right)
            if node.left:
                queue.enqueue_front(node.left)
            # Because of this order, this prints what's IMMEDIATELY left
            # then go deeper left before going right



        return visit

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            items = self._traverse_post_order_iterative(self.root, items)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_post_order_recursive(node.left, visit)
        # TODO: Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_post_order_recursive(node.right, visit)
        # TODO: Visit this node's data with given function
        visit.append(node.data)
        return visit

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)
        queue = DeQueue()
        queue.enqueue_front(node)

        while queue.length() > 0:
            while node.right is not None:
                queue.enqueue_front(node)
                node = node.right
            else:
                node = queue.dequeue_front()
                if node.right:
                    node = node.right
                    print(node)


        return visit

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            items = self._traverse_level_order_iterative(self.root, items)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Create queue to store nodes not yet traversed in level-order
        queue = DeQueue()
        # TODO: Enqueue given starting node
        queue.enqueue_front(start_node)
        # TODO: Loop until queue is empty
        while queue.length() > 0:
            # TODO: Dequeue node at front of queue
            node = queue.dequeue_front()
            # TODO: Visit this node's data with given function
            visit.append(node.data)
            # TODO: Enqueue this node's left child, if it exists
            if node.left:
                queue.enqueue_back(node.left)
            # TODO: Enqueue this node's right child, if it exists
            if node.right:
                queue.enqueue_back(node.right)
        return visit

def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    # items = [4, 2, 6, 1, 3, 5, 7]
    items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}, height: {}'.format(item, tree.size, tree.height()))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
