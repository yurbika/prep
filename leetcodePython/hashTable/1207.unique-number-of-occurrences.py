class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        found = []
        for i in arr:
            if count.get(arr.count(i), 0) == 0 or i in found:
                count[arr.count(i)] = i
                found.append(i)
            else:
                return False
        return True
