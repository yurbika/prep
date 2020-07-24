import unittest


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


root = NodeB(4)
root.left = NodeB(1)
root.right = NodeB(5)

# left side
root.left.left = NodeB(0)
root.left.right = NodeB(2)

# right side
root.right.right = NodeB(6)

root.display()


# 000: [4, 1, 0, 2, 5, 6]
# 001: [4, 1, 0, 5, 2, 6]
# 002: [4, 1, 0, 5, 6, 2]
# 003: [4, 1, 5, 0, 2, 6]
# 004: [4, 1, 5, 0, 6, 2]
# 005: [4, 1, 5, 6, 0, 2]
# 006: [4, 5, 1, 0, 2, 6]
# 007: [4, 5, 1, 0, 6, 2]
# 008: [4, 5, 1, 6, 0, 2]
# 009: [4, 5, 6, 1, 0, 2]
# 010: [4, 1, 2, 0, 5, 6]
# 011: [4, 1, 2, 5, 0, 6]
# 012: [4, 1, 2, 5, 6, 0]
# 013: [4, 1, 5, 2, 0, 6]
# 014: [4, 1, 5, 2, 6, 0]
# 015: [4, 1, 5, 6, 2, 0]
# 016: [4, 5, 1, 2, 0, 6]
# 017: [4, 5, 1, 2, 6, 0]
# 018: [4, 5, 1, 6, 2, 0]
# 019: [4, 5, 6, 1, 2, 0]


def wave(left, right, prefix, result):
    if not left or not right:
        result.append(prefix + left + right)
        return

    head = left[0]

    # dont modify left bcs we maybe need it later again
    left_tail = left[1:]

    # recursion
    wave(left_tail, right, prefix+[head], result)

    head = right[0]

    # dont modify right bcs we maybe need it later again
    right_tail = right[1:]

    # recursion
    wave(left, right_tail, prefix+[head], result)


def sequences(root):
    result = []
    if not root:
        result.append([])
        return result

    prefix = []
    prefix.append(root.val)
    left = sequences(root.left)
    right = sequences(root.right)

    for i in left:
        for j in right:
            temp = []
            wave(i, j, prefix, temp)
            result += temp

    return result


for i in sequences(root):
    print(i, end="\n")
