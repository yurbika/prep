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


root = NodeB(10)
root.left = NodeB(5)
root.right = NodeB(-3)
# left side
root.left.left = NodeB(3)
root.left.left.right = NodeB(-2)

root.left.left.left = NodeB(3)
root.left.right = NodeB(2)
root.left.right.right = NodeB(1)


# right side
root.right.right = NodeB(11)

root.display()


def pathUtilFunction(node, count, targetSum, pathSum, hashTable):
    if not node:
        return 0

    pathSum = pathSum + node.val

    if pathSum in hashTable:
        hashTable[pathSum] += 1
    else:
        hashTable[pathSum] = 1

    # if the root is equal to targetSum
    # backslash is for multiline addition
    # parentheses for comments between multiline addition
    count = (int(pathSum == targetSum) + \
             # check if we found a path
             hashTable.get(pathSum - targetSum, 0) + \
             # recursion left side
             pathUtilFunction(node.left, count, targetSum, pathSum, hashTable) + \
             # recursion right side
             pathUtilFunction(node.right, count, targetSum, pathSum, hashTable))
    # delete on the way back
    hashTable[pathSum] -= 1
    return count


def pathWithSum(root, targetSum):
    hashTable = {}
    return pathUtilFunction(root, 0, targetSum, 0, hashTable)


print(pathWithSum(root, 10))
