#write a method to replace all spaces in a string with "%20". You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string

#version 1
string="Mr John Smith    "

print(string.strip().replace(" ","%20"))

#version 2

arr = list(string)

i = len(arr) - 1
j = i

#skip buffer
while arr[i] == " ":
    i-=1

while i != j:
    if arr[i] == " ":
        arr[j-2]="%"
        arr[j-1]="2"
        arr[j]="0"
        j-=2
    else:
        arr[j] = arr[i]
    j-=1
    i-=1


print(''.join(arr))