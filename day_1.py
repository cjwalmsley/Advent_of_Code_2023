#https://adventofcode.com/2023/day/1

def filter_numeric(a_string):
    return list(filter(lambda a_character: a_character.isnumeric(), a_string))

import functools
try:
    file = open("input.txt", "r")
    input = file.readlines()
finally:
    file.close()

#input = [make_numeric(row) for row in input]

input = [filter_numeric(row) for row in input]

print(functools.reduce(lambda first, last: first + last, [int(row[0] + (row[-1])) for row in input]))