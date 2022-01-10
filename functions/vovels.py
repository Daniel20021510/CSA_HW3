vowels = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}


def count_vowels(line):
    vowels_number = 0
    for i in line:
        for j in vowels:
            if (i == j):
                vowels_number += 1
    return vowels_number
