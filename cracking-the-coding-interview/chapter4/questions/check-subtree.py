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


t2 = NodeB(4)
t2.left = NodeB(1)
t2.right = NodeB(5)

# left side
t2.left.left = NodeB(0)
t2.left.right = NodeB(2)

# right side
t2.right.right = NodeB(6)

t2.display()

t1 = NodeB(1)
t1.left = NodeB(3)
t1.right = NodeB(18)
# left side
t1.left.left = NodeB(90)
t1.left.left.right = NodeB(450)
t1.left.left.left = NodeB(71)
t1.left.right = NodeB(21)
t1.left.right.left = NodeB(17)
t1.left.right.right = NodeB(5)
# right side
t1.right.left = NodeB(2)
t1.right.right = NodeB(1)
t1.right.left.left = NodeB(9)
t1.right.left.right = NodeB(101)
t1.right.right.right = NodeB(0)
#t1.right.right.right.right = NodeB(6)
#t1.right.right.left = NodeB(1)
#t1.right.right.left.left = NodeB(0)
#t1.right.right.left.right = NodeB(2)


t1.display()


def equalTree(t1, t2, equal):
    if not t1 and t2 or not t2 and t1:
        return False

    if not t1 or not t2:
        return True

    if t1.val == t2.val:
        equal = equalTree(t1.left, t2.left, equal)
        equal = equalTree(t1.right, t2.right, equal)
    else:
        equal = False

    return equal


def checkSubtree(t1, t2, found):
    if not t1 or not t2:
        return False
    if found:
        return True

    if equalTree(t1, t2, False):
        return True

    found = checkSubtree(t1.right, t2, found)
    if found:
        return True
    found = checkSubtree(t1.left, t2, found)
    if found:
        return True
    found = checkSubtree(t1, t2.left, found)
    if found:
        return True
    found = checkSubtree(t1, t2.right, found)

    return found


print(checkSubtree(t1, t2, False))
