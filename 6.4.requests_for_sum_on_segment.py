class Node(object):
    """Node object for AVLTree.
    """
    def __init__(self, key: int) -> None:
        """Instantiates Node object for AVLTree.
        Parent, left and right are pointers to parent and child nodes.
        Height initialized at 1, adjusted with insert and delete to represent height of node. Null nodes have
        height of 0.
        The sum is initialized at key, adjusted with insert and delete to represent
        the sum of the keys of the nodes in the subtree. Null nodes have sum of 0.
        """
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1
        self.sum = key


class AVLTree(object):
    """AVLTree/Balanced Binary Search Tree Data structure.
    """

    def __init__(self):
        """Tree is represented by its root node, initially None.
         The following methods are implemented:
             Create a new tree:
                 tree = AVLTree()
             View tree structure:
                 tree.display()
             Search for key in tree:
                 tree.search(key)
                 Returns a response: Found or Not found.
             Insert key into tree:
                 tree.insert(key)
             Delete key from tree:
                 tree.delete(key)
             Calculate the sum of all elements of the set
             that fall into the interval [l, r]:
                 tree.calc_sum_on_segment(l, r)
     """
        self.root = None
        self.last_sum = 0

    def _get_root(self) -> 'Node':
        """Returns root node.
        :return: Root node of tree.
        """
        if self.root:
            while self.root.parent:
                self.root = self.root.parent
        return self.root

    def _hash(self, key: int) -> int:
        """Calculates the hashed value.
        Before any operation is performed, each key is hashed.
        :return: int. Hashed key.
        """
        return (key + self.last_sum) % 1000000001

    def search(self, key: int) -> str:
        """User interface for search method.
        Calls _find_node with root from _get_root.
        :param key: Not hashed key to be found in tree.
        :return: string. "Found" if key in tree, else, "Not found".
        """
        key = self._hash(key)
        root = self._get_root()
        result = self._find_node(root, key) if root else False
        return 'Found' if result else 'Not found'

    def _find_node(self, cur_node: 'Node', key: int) -> 'Node':
        """Finds and returns node with given key, else, returns None.
        :param cur_node: Root node from _get_root.
        :param key: Key contained within node to be found.
        :return: Node containing key if such a node exists, else, None.
        """
        if cur_node and key == cur_node.key:
            return cur_node
        elif cur_node and key < cur_node.key:
            return self._find_node(cur_node.left, key)
        elif cur_node and key > cur_node.key:
            return self._find_node(cur_node.right, key)
        return None

    def insert(self, key: int) -> None:
        """User interface for inserting key into tree.
        Tree root is created on first insertion.
        Calls _insert with root provided by _get_root.
        Resets root after insert in case rotation changes root.
        :param key: Not hashed key to be inserted into tree.
        :return:
        """
        key = self._hash(key)
        root = self._get_root()
        if not root:
            self.root = Node(key)
        else:
            self._insert(root, key)
            self.root = self._get_root()

    def _insert(self, cur_node: 'Node', key: int) -> None:
        """Inserts key into tree.
        Calls _inspect_insertion to determine if insertion caused tree imbalance.
        :param cur_node: Root of tree.
        :param key: Key to insert into tree.
        :return:
        """
        if key < cur_node.key:
            if not cur_node.left:
                cur_node.left = Node(key)
                cur_node.left.parent = cur_node
                self._inspect_insertion(cur_node.left, [])
            else:
                self._insert(cur_node.left, key)

        elif key > cur_node.key:
            if not cur_node.right:
                cur_node.right = Node(key)
                cur_node.right.parent = cur_node
                self._inspect_insertion(cur_node.right, [])
            else:
                self._insert(cur_node.right, key)

    def _inspect_insertion(self, cur_node: 'Node', nodes: list) -> None:
        """Determines if insertion creates need to balance sub-tree.
        Rebalance needed if difference in height of child nodes is > 1.
        Creates list of nodes to be rotated if above condition is true.
        Calls _rebalance_node with nodes to be balanced.
        :param cur_node: The newly inserted node.
        :param nodes: Empty list.
        :return:
        """
        par = cur_node.parent
        if not par:
            return

        nodes = [cur_node] + nodes

        left, right = self._get_height(par.left), self._get_height(par.right)
        if abs(left - right) > 1 and len(nodes) > 1:
            nodes_for_rebalance = [par] + nodes
            self._rebalance_node(*nodes_for_rebalance[:3])
            par = cur_node.parent

        if not par:
            return

        new_height = 1 + max(self._get_height(par.left), self._get_height(par.right))
        if new_height != par.height:
            par.height = new_height

        new_sum = par.key + self._get_sum(par.left) + self._get_sum(par.right)
        if new_sum != par.sum:
            par.sum = new_sum

        self._inspect_insertion(par, nodes)

    def _get_height(self, cur_node: 'Node') -> int:
        """ Gets height of cur_node. Returns 0 if node is None else returns node.height.
        :param cur_node: Node
        :return: Node.height
        """
        return cur_node.height if cur_node else 0

    def _get_sum(self, cur_node: 'Node') -> int:
        """ Gets sum of cur_node. Returns 0 if node is None else returns node.sum.
        :param cur_node: Node
        :return: Node.sum
        """
        return cur_node.sum if cur_node else 0

    def _rebalance_node(self, z: 'Node', y: 'Node', x: 'Node') -> None:
        """Determines orientation of imbalanced nodes and calls indicated balancing methods.
        Calls _rotate_right or _rotate_left as determined by orientation of unbalanced nodes.
        :param z: Highest node. Rebalance occurs 'around' this node.
        :param y: Child of z
        :param x: Child of y
        """
        if y == z.left and x == y.left:
            """    z
                  /
                 y
                /
               x   """
            self._right_rotate(z)

        elif y == z.left and x == y.right:
            """   z
                 /
                y 
                 \
                  x  """
            self._left_rotate(y)
            self._right_rotate(z)

        elif y == z.right and x == y.right:
            """   z
                   \
                     y 
                      \
                        x  """
            self._left_rotate(z)

        elif y == z.right and x == y.left:
            """   z
                    \
                      y
                    /
                  x  """
            self._right_rotate(y)
            self._left_rotate(z)

        #else:
        #    raise Exception('Tree corrupted')

    def _right_rotate(self, z: 'Node') -> None:
        """Rotates around z to rebalance sub-tree.
        Makes z the right child of y.
        The parent of z (par) becomes the parent of y.
        The right child of y (b) becomes the left child of z.
        :param z: Root of sub-tree to be balanced.
        """
        """    z            y
              / \          / \
             y   c   ->   a   z
            / \              / \
           a   b            b   c   
        """
        par, y = z.parent, z.left
        b = y.right

        y.parent, y.right = par, z
        z.parent = y

        z.left = b
        if b: b.parent = z

        if y.parent:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        z.sum = z.key + self._get_sum(z.left) + self._get_sum(z.right)
        y.sum = y.key + self._get_sum(y.left) + self._get_sum(y.right)

    def _left_rotate(self, z: 'Node') -> None:
        """Rotates around z to rebalance sub-tree.
        Makes z the left child of y.
        The parent of z (par) becomes the parent of y.
        The left child of y (b) becomes the right child of z.
        :param z: Root of sub-tree to be balanced.
        """
        """    z            y
              / \          / \
             a   y   ->   z   c
                / \      / \
               b   c    a   b   
        """
        par, y = z.parent, z.right
        b = y.left

        y.parent, y.left = par, z
        z.parent = y

        z.right = b
        if b: b.parent = z

        if y.parent:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        z.sum = z.key + self._get_sum(z.left) + self._get_sum(z.right)
        y.sum = y.key + self._get_sum(y.left) + self._get_sum(y.right)

    def delete(self, key: int) -> None:
        """User interface for deleting key into tree.
        Calls _find_node with root from _get_root.
        If root is to be deleted and has no children, root is set to None.
        Calls _delete(node). If _delete(node) returns a node it is the new root node.
        :param key: Not hashed key to delete from tree.
        :return:
        """
        key = self._hash(key)
        root = self._get_root()
        node = self._find_node(root, key)
        if node:
            if node == root and (not root.left and not root.right):
                self.root = None
            else:
                result = self._delete(node)
                self.root = result if result else self._get_root()

    def _delete(self, node: 'Node') -> 'Node':
        """ Deletes node found in _find_node.
        Removes nodes and handles deleted node's orphaned children, if any.
        Deleted nodes with two children are handled by finding the smallest relative of the deleted node's right child,
        replacing the to-be-deleted node's key with that of its smaller relative, then marking the smaller relative
        to be deleted instead.
        Calls _inspect_deletion to ensure proper balancing of sub-tree after deletion.
        :param node: Node to be deleted.
        :return: New root Node, if necessary.
        """

        def smallest_node(cur_node: 'Node') -> 'Node':
            """Finds smallest relative of cur_node.
            :param cur_node: A Node.
            :return: Relative of cur_node with smallest value.
            """
            while cur_node.left:
                cur_node = cur_node.left
            return cur_node

        def num_children(cur_node: 'Node'):
            """Finds number of cur_node's children.
            :param cur_node: A node
            :return: Number of cur_node's children.
            """
            num = 0
            if cur_node.left:
                num += 1
            if cur_node.right:
                num += 1
            return num

        node_parent = node.parent
        num_node_children = num_children(node)

        # Leaf nodes may simply be deleted.
        if num_node_children == 0:
            if node_parent:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
                self._inspect_deletion(node_parent)

        # Parent of deleted node made parent of deleted node's child.
        if num_node_children == 1:
            child = node.left if node.left else node.right
            if node_parent:
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
                child.parent = node_parent
                self._inspect_deletion(node_parent)
            else:
                child.parent = node_parent
                return child  # returned to promote child to root node

        # If the node to be deleted has 2 children, the key of its next greater relative is promoted to the
        # to-be-deleted node. The relative is then deleted instead.
        if num_node_children == 2:
            successor = smallest_node(node.right)
            successor_parent = successor.parent
            node.key = successor.key
            self._delete(successor)
            self._inspect_deletion(successor_parent)

    def _inspect_deletion(self, cur_node: 'Node') -> None:
        """Ensures tree is balanced after deletion.
        Calls _rebalance_node if imbalance is detected.
        Calls _inspect_insertion to ensure balance up the tree.
        :param cur_node: Node. Parent of deleted node.
        :return:
        """

        def taller_child(node: 'Node') -> 'Node':
            """Finds taller of node's children.
            :param node: Node. Node to be inspected.
            :return: Node. Child of node with greater height.
            """
            left_height = self._get_height(node.left)
            right_height = self._get_height(node.right)
            return node.left if left_height >= right_height else node.right

        cur_node.height = 1 + max(self._get_height(cur_node.left), self._get_height(cur_node.right))
        cur_node.sum = cur_node.key + self._get_sum(cur_node.left) + self._get_sum(cur_node.right)

        left, right = self._get_height(cur_node.left), self._get_height(cur_node.right)
        if abs(left - right) > 1:
            y = taller_child(cur_node)
            x = taller_child(y)
            self._rebalance_node(cur_node, y, x)

        self._inspect_insertion(cur_node, [])

    def calc_sum_on_segment(self, l: int, r: int) -> int:
        """User interface for calculating the sum on a segment.
        The sum of elements on the segment is calculated according to the formula:
        the sum of elements greater than l (not including l)
        + l (if l is included in the segment)
        - the sum of elements greater than r (not including r).
        :param l: Not hashed value of the left border of the segment.
        :param r: Not hashed value of the right border of the segment.
        :return: the sum on a segment.
        """
        l, r = self._hash(l), self._hash(r)
        found_l, less_l, greater_l = self._find_less_greater_sum(l)
        found_r, less_r, greater_r = self._find_less_greater_sum(r)
        sum = greater_l + (l if found_l else 0) - greater_r
        self.last_sum = sum
        return sum

    def _find_less_greater_sum(self, key: int) -> (int, int, int):
        """Finds and returns a tuple of values needed to calculate the sum on a segment.
        :param key: Key contained within node to be found.
        :return: (found, less_sum, greater_sum).
        found - bool. True if key in tree, else, False.
        less_sum - int. The sum of elements less than key (not including key).
        greater_sum - int. The sum of elements greater than key (not including key).
        """
        node = self._get_root()
        found = False
        less_sum, greater_sum = 0, 0

        while node:
            if key < node.key:
                if node.right:
                    greater_sum += node.right.sum
                greater_sum += node.key
                node = node.left
            elif key > node.key:
                if node.left:
                    less_sum += node.left.sum
                less_sum += node.key
                node = node.right
            else:
                found = True
                break
        if found:
            if node.left:
                less_sum += node.left.sum
            if node.right:
                greater_sum += node.right.sum

        return found, less_sum, greater_sum

    def display(self) -> None:
        """User interface for viewing tree structure.
        Each node is displayed as a set: key/(height,sum).
        :return:
        """
        root = self._get_root()
        if root:
            lines, *_ = self.display_aux(root)
            print('\n'.join(lines))

    def display_aux(self, node: 'Node'):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '{key}/({height},{sum})'.format(key=node.key, height=node.height, sum=node.sum)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self.display_aux(node.left)
            s = '{key}/({height},{sum})'.format(key=node.key, height=node.height, sum=node.sum)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self.display_aux(node.right)
            s = '{key}/({height},{sum})'.format(key=node.key, height=node.height, sum=node.sum)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.display_aux(node.left)
        right, m, q, y = self.display_aux(node.right)
        s = '{key}/({height},{sum})'.format(key=node.key, height=node.height, sum=node.sum)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def main():

    # tree initialization
    tree = AVLTree()
    output = []

    # read the number of requests
    n = int(input())

    # read requests
    for _ in range(n):
        req = input().split()
        operation, param = req[0], int(req[1])

        # process the request "+ f(i)"
        if operation == "+":
            tree.insert(param)
            #print('insert %s' % param)
            #tree.display()

        # process the request "- f(i)"
        elif operation == "-":
            tree.delete(param)
            #print('delete %s' % param)
            #tree.display()

        # process the request "? f(i)"
        elif operation == "?":
            result = tree.search(param)
            output.append(result)
            #print('%s %s' % (result, param))

        # process the request "s f(l) f(r)"
        elif operation == "s":
            l, r = param, int(req[2])
            sum = tree.calc_sum_on_segment(l, r)
            output.append(str(sum))
            #print('sum from %s to %s = %s' % (l, r, sum))

    print('\n'.join(output))


if __name__ == "__main__":
    main()