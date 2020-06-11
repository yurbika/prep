# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------


import string

n = int(input())
alpha = string.ascii_lowercase
ans = []

for i in range(n):
    s = "-".join(alpha[i:n])
    ans.append((s[::-1]+s[1:]).center(n * 4 - 3, "-"))

print("\n".join(ans[:0:-1]+ans))
