string = "aaaaaaabbccsddfffddddddddssaaazzuuzdsdgdg"

def stringCompression(string):
    solution = ""
    counter = 1

    for index,i in enumerate(string):
        if len(string) == 1:
            return string
        
        if index + 1 < len(string) and string[index] == string[index+1]:
            counter += 1
        else:
            solution = f"{solution}{string[index]}{counter}"
            counter = 1

    if len(solution) >= len(string):
        return string

    return solution

print(stringCompression(string))