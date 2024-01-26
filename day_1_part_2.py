#https://adventofcode.com/2023/day/1#part2
import day_1
import re as re
def parse_numbers(a_string):
    number_map = {'one': '1',
                  'two': '2',
                  'three': '3',
                  'four': '4',
                  'five': '5',
                  'six': '6',
                  'seven': '7',
                  'eight': '8',
                  'nine': '9'}
    number_items_to_replace = []
    for item in number_map.items():
        if item[0] in a_string:
            for each_substring in range(len(re.findall(item[0], a_string))):
                number_items_to_replace.append((item[0], item[-1], a_string.find(item[0])))
                number_items_to_replace.append((item[0], item[-1], a_string.rfind(item[0])))
    # sort the items by index
    number_items_to_replace.sort(key=lambda item: item[-1])
    if len(number_items_to_replace) > 0:
        first_item = number_items_to_replace[0]
        last_item = number_items_to_replace[-1]
        a_string = a_string.replace(first_item[0], first_item[1])
        a_string = a_string.replace(last_item[0], last_item[1])

    return a_string
def parse_numbers_for_rows(an_array):
    return [parse_numbers(a_row) for a_row in an_array]
def day_1_part_2():
    input = day_1.read_file('input.txt')
    input = parse_numbers_for_rows(input)
    input = day_1.convert_to_numeric(input)
    return day_1.sum_first_and_last(input)

print(day_1_part_2())