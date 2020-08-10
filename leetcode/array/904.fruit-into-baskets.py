class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not tree:
            return []
        if len(tree) <= 2:
            return len(tree)

        i = 0
        j = 1
        result = [tree[i]]
        maxValue = 0
        while j < len(tree):
            if tree[j] in result:
                result.append(tree[j])
                j += 1
            elif tree[j] not in result and len(set(result)) != 2:
                result.append(tree[j])
                j += 1
            elif tree[j] not in result and len(set(result)) == 2:
                if maxValue < len(result):
                    maxValue = len(result)
                i = j-1
                while tree[i-1] == tree[i]:
                    i -= 1
                j = i+1
                result = [tree[i]]
            else:
                j += 1
        if len(result) > maxValue:
            maxValue = len(result)
        return maxValue
