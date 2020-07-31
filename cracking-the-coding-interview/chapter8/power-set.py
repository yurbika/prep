def powerSet(sets, memo):
    if not sets:
        return memo

    currValue = sets.pop(0)
    memo = memo+[ele+[currValue] for ele in memo]
    memo = powerSet(sets, memo)
    return memo


print(powerSet(['a', 'b', 'c', 'd', 'e', 'f'], [[]]))
