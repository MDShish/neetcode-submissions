from typing import List

def read_integers() -> List[int]:
    number_string = input()
    string_list = [int(x) for x in number_string.split(",")]
    return string_list
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())