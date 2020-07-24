projects = ["a", "b", "c", "d", "e", "f"]

dependencies = [("a", "d"), ("a", "f"), ("f", "b"),
                ("b", "d"), ("f", "a"), ("d", "c")]


def buildOrder(p, d):
    dictonary = {ele: [] for ele in p}
    solution = []
    visited = []

    for i in d:
        dictonary[i[1]].append(i[0])

    for i in dictonary:
        if dictonary[i] == []:
            solution.append(i)

    for i in solution:
        dictonary.pop(i)

    while dictonary:
        for i in dictonary:
            s1 = set(dictonary[i])
            s2 = set(solution)
            if s1.issubset(s2):
                solution.append(i)
                if i in visited:
                    visited.remove(i)
            else:
                if i in visited:
                    raise Exception("Cant build project")
                else:
                    visited.append(i)

        for i in solution:
            if i in dictonary:
                dictonary.pop(i)

    return solution


print(buildOrder(projects, dependencies))
