class NodeB:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the t2."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Bts:
    def __init__(self):
        self.root = None

    def __repr__(self):
        self.root.display()
        return ""

    def _insert(self, val, root):
        # find pos
        if root.right is not None and val > root.val:
            self._insert(val, root.right)
        elif root.left is not None and val < root.val:
            self._insert(val, root.left)

        # insert
        if root.right is None and val > root.val:
            root.right = NodeB(val)
            return
        elif root.left is None and val < root.val:
            root.left = NodeB(val)
            return

    def insert(self, val):
        if self.root is None:
            self.root = NodeB(val)
        else:
            self._insert(val, self.root)

    def _find(self, root, val, found):
        if not root:
            return False

        if val == root.val:
            return True

        found = self._find(root.left, val, False)
        found = self._find(root.right, val, False)

        return found

    def find(self, val):
        return self._find(self.root, val, False)

    def _successor(self, node):
        n = node
        successor = None
        while n:
            n = n.right
            while n:
                if n.val > node.val:
                    successor = n.val
                n = n.left
            if successor:
                return successor

        n = node
        while n:
            n = n.parent
            if n and n.val > node.val:
                return n.val
        return successor

    def _delete(self, root, val):
        if not root:
            return

        # case 0 root is val
        if root.val == val:
            root.val = self._successor(root)
            self._delete(root.right, root.val)

        # case 1 no children
        if root.right and root.right.val == val and not root.right.right and not root.right.left:
            root.right = None
            return

        if root.left and root.left.val == val and not root.left.right and not root.left.left:
            root.left = None
            return

        # case 2 one children
        if root.right and root.right.val == val and root.right.right and not root.right.left:
            root.right = root.right.right
            return
        if root.right and root.right.val == val and not root.right.right and root.right.left:
            root.right = root.right.left
            return

        if root.left and root.left.val == val and root.left.right and not root.left.left:
            root.left = root.left.right
            return

        if root.left and root.left.val == val and not root.left.right and root.left.left:
            root.left = root.left.left
            return

        # case 3 two children
        if root.right and root.right.val == val and root.right.right and root.right.left:
            root.right.val = self._successor(root.right)
            self._delete(root.right.right, root.right.val)
            return

        if root.left and root.left.val == val and root.left.right and root.left.left:
            root.left.val = self._successor(root.left)
            self._delete(root.left.right, root.left.val)
            return

        if val > root.val:
            self._delete(root.right, val)
        if val < root.val:
            self._delete(root.left, val)

    def delete(self, val):
        self._delete(self.root, val)

    def getRandomNode(self):
        pass


root = NodeB(35)
root.left = NodeB(30)
root.left.parent = root
root.right = NodeB(40)
root.right.parent = root

# left side
root.left.left = NodeB(27)
root.left.left.parent = root.left

root.left.left.left = NodeB(26)
root.left.left.left.parent = root.left.left

root.left.right = NodeB(33)
root.left.right.parent = root.left

root.left.right.left = NodeB(31)
root.left.right.left.parent = root.left.right

root.left.right.right = NodeB(34)
root.left.right.right.parent = root.left.right

# right side
root.right.left = NodeB(37)
root.right.left.parent = root.right

root.right.right = NodeB(50)
root.right.right.parent = root.right

root.right.left.left = NodeB(36)
root.right.left.left.parent = root.right.left

root.right.left.right = NodeB(39)
root.right.left.right.parent = root.right.left

root.right.right.right = NodeB(60)
root.right.right.right.parent = root.right.right

root.right.right.left = NodeB(49)
root.right.right.left.parent = root.right.right

root.right.right.left.left = NodeB(46)
root.right.right.left.left.parent = root.right.right.left


bts = Bts()
bts.root = root
print(bts.find(7))
print("\n")
print(bts)
bts.delete(40)

print(bts)
