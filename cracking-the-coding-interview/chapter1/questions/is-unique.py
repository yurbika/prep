#Implement an algorithm to determein if a string has all unique characters. What if you canot use additional data structures?

string= "iüweewrnmvcnböxyxfcutaapioa"
arr = [[] for i in range(128)]

def testString(string):
    for index,c in enumerate(string):
        if len(string) > 128:
            return False
        elif len(arr[ord(c) % 128])>0:
            return f"{index} {c}"
        arr[ord(c) % 128 ].append(c)


print(testString(string))
