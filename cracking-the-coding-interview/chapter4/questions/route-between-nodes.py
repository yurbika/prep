class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def __repr__(self):
        return self.val

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        node = self.head
        nodes=[]

        while node is not None:
            nodes.append(f"{node.val}")
            node = node.next

        return "->".join(nodes)    
    
    def is_empty(self):
        return self.head is None
    
    def remove(self):
        n = self.head
        if self.is_empty():
            return None
        if n.next is None:
            temp = n.val
            n.val = None
            n = None
            return temp
        while n.next.next is not None:
            n = n.next
        temp = n.next.val
        n.next = None
        return temp

    def push(self,val):
        temp = self.head
        self.head = Node(val)
        self.head.next = temp
        self.size += 1
        
    def peek(self):
        if self.is_empty():
            return None

        n = self.head.val
        while n.next is not None:
            n = n.next

        return n.val

graph = {
'A':['B', 'C', 'D'],
'B':['E', 'F'],
'C':['G'],
'G':['H'],
'I':['Z']
}

start = 'I'
target = 'A'

#recursive way dfs
def dfs(graph,visited,node,target):
    if node not in visited and node in graph:
        visited.append(node)
        for n in graph.get(node,[]):
            dfs(graph,visited,n,target)
    elif node not in graph:
        visited.append(node)
    return target in visited

print("recursive dfs: ",dfs(graph,[],start,target))

#iterative dfs
def dfs(graph,node,target):
    stack = [node]
    visited = []

    while stack:
        curr = stack.pop(0)
        if curr == target:
            return True
        if curr not in visited:
            visited.append(curr)
            stack = graph.get(curr,[]) + stack

    return False


print("iterative dfs: ",dfs(graph,start,target))


def bfs(graph,node,target):
    queue = Queue()
    queue.head = Node(node)
    visited = []
    curr = queue.remove()

    while not queue.is_empty() and curr:
        if curr == target:
            return True
        tempArr = (graph.get(curr,[]))[:]
        while tempArr:
            queue.push(tempArr.pop(0))
        if curr not in visited:
            visited.append(curr)
            curr = queue.remove()
            if curr == None:
                curr = queue.remove()

        else:
            curr = queue.remove()
    return False

print("bfs: ",bfs(graph,start,target))