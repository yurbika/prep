#given a string, write a function to check if it is a permutation of a palindrome.

string = "malayalam"

def is_palindrome_permutation(string):
    string = string.lower().replace(" ","")
    odd_counter = 0
    arr = [0] * 128

    for i in string:
        arr[ord(i) - ord("a")] +=1


    for i in arr:
        if i % 2 == 1:
            odd_counter += 1
        if odd_counter > 1:
            return False
        
    if odd_counter <= 1:
        return True


print(is_palindrome_permutation(string))