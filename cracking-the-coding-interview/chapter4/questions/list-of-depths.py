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

root.display()


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

    def __repr__(self):
        return f"{self.val}"


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        if isinstance(node, Node):
            while node is not None:
                nodes.append(f"{node.val}")
                node = node.next
        else:
            nodes.append(f"{node}")

        nodes.append("None")
        return "->".join(nodes)

    def insert_end(self, node):
        n = self.head
        while n is not None:
            if n.next == None:
                break
            n = n.next
        n.next = node
        node.prev = n


# solution
def getChildren(root, target, solution):
    if root is not None and root.val == target:
        if root.left is not None and root.right is not None:
            solution += [root.left.val, root.right.val]
        elif root.left is not None:
            solution += [root.left.val]
        elif root.right is not None:
            solution += [root.right.val]

    else:
        if root:
            getChildren(root.left, target, solution)
            getChildren(root.right, target, solution)

    return solution


def listOfDepths(root):
    solution = []
    queue = []
    queue.append(root.val)
    level = 0
    while queue:
        if level == 0:
            llist = LinkedList()
            llist.head = queue.pop(0)
            solution.append(llist)
            queue += [root.left.val, root.right.val]
            level += 1
        else:
            temp = []
            for i in queue:
                temp += getChildren(root, i, [])
            llist = LinkedList()
            llist.head = Node(queue.pop(0))
            while queue:
                llist.insert_end(Node(queue.pop(0)))
            queue = temp[:]
            solution.append(llist)
    return solution


lod = listOfDepths(root)

print("\n")
for i in lod:
    print(i)
