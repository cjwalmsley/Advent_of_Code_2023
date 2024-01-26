#https://adventofcode.com/2023/day/1
import functools
def filter_numeric(a_string):
    return list(filter(lambda a_character: a_character.isnumeric(), a_string))
def read_file(a_filename):
    try:
        file = open(a_filename, 'r')
        input = file.readlines()
    finally:
        file.close()
    return input

def filter_numeric(a_string):
        return list(filter(lambda a_character: a_character.isnumeric(), a_string))
def convert_to_numeric(an_array):
    return [filter_numeric(a_string) for a_string in an_array]
def sum_first_and_last(an_array):
    return functools.reduce(lambda first, last: first + last, [int(row[0] + (row[-1])) for row in an_array])
def day_1():
    input = read_file('input.txt')
    input = convert_to_numeric(input)
    return sum_first_and_last(input)

print(day_1())