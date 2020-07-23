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
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
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


root = NodeB(1)
root.left = NodeB(3)
root.right = NodeB(18)
# left side
root.left.left = NodeB(90)
root.left.left.right = NodeB(450)
root.left.left.left = NodeB(71)
root.left.right = NodeB(21)
root.left.right.left = NodeB(17)
root.left.right.right = NodeB(5)
# right side
root.right.left = NodeB(2)
root.right.right = NodeB(11)
root.right.left.left = NodeB(9)
root.right.left.right = NodeB(101)
root.right.right.right = NodeB(8)
root.right.right.left = NodeB(201)
root.right.right.left.left = NodeB(555)
root.right.right.left.left.left = NodeB(1297)
#root.right.right.left.left.left.left = NodeB(497)
#root.right.right.left.left.left.left = NodeB(8297)


root.display()


def getHeight(n):
    if n == None:
        return 0

    right = getHeight(n.right)
    left = getHeight(n.left)

    if left == -1 or right == -1:
        return -1

    if abs(left - right) > 1:
        return -1

    return max(left, right) + 1


def checkBalanced(root):
    temp = getHeight(root)
    print(temp)
    return temp > -1


print(checkBalanced(root))
