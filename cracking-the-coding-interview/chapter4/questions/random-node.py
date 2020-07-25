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
        if self._find(self.root, val, False):
            return f"{val} is in the Tree"
        else:
            return f"{val} is not in the Tree"

    def delete(self, val):
        pass

    def getRandomNode(self):
        pass


bts2 = Bts()
bts2.insert(4)
bts2.insert(1)
bts2.insert(0)
bts2.insert(2)
bts2.insert(5)
bts2.insert(6)

print(bts2.find(7))

print(bts2)
