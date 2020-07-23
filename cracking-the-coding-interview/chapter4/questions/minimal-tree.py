import random


arr = [*(random.randint(1, 1000) for _ in range(27))]

arr.sort()

length = len(arr)


class Node:
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


def createArray(array, result):
    if array == []:
        return result
    result.append(array[round(len(array)/2)])
    array.pop(round(len(array)/2))
    createArray(array, result)
    return result


def createMinTreeUtil(root, arr, mid):
    for i in range(len(arr)):
        val = arr[i]
        if val != mid:
            n = root
            while n is not None:
                if n.val > val:
                    if n.left is None:
                        n.left = Node(val)
                        break
                    else:
                        n = n.left
                else:
                    if n.right is None:
                        n.right = Node(val)
                        break
                    n = n.right


def createMinTree(array):
    length = len(array)
    mid = array[round(length/2)]
    root = Node(mid)

    arr1 = createArray(array[:round(length/2)], [])
    arr2 = createArray(array[round(length/2)+1:], [])

    createMinTreeUtil(root, arr1, mid)
    createMinTreeUtil(root, arr2, mid)
    return root


createMinTree(arr).display()
