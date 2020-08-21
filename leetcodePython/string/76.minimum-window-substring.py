def minWindow(s, t):
    if len(t) > len(s):
        return ''
    need = {ele: 0 for ele in t}
    missing = 0
    for i in t:
        need[i] += 1
        missing += 1

    i = 0
    start = 0
    end = 0

    for j, char in enumerate(s, 1):
        if need.get(char, None) is not None:
            need[char] -= 1
            if need[char] >= 0:
                missing -= 1
            if missing == 0:
                while i < j and (need.get(s[i], None) is None or need.get(s[i], None) < 0):
                    if need.get(s[i], None) is not None:
                        need[s[i]] += 1
                    i += 1
                if not end or j - i <= end - start:
                    start, end = i, j
    return s[start:end]


print(minWindow("ADOBECODEBANC", 'ABC'))
