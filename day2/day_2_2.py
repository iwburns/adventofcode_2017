#!/usr/bin/python3

import fileinput
import re
import itertools

def get_lines(file_name):
	return fileinput.input(files=(file_name))

def get_checksum(lines):
	total = 0

	for line in lines:
		line = re.split(r'\t+| +', line.rstrip('\n'))
		line = list(map(int, line))

		combos = itertools.combinations(line, 2)

		for combo in combos:
			larger = max(combo)
			smaller = min(combo)

			ratio = larger / smaller
			if (ratio).is_integer():
				total += int(ratio)
				break

	return total

def print_solution():
	print(get_checksum(get_lines('day2/input.txt')))

print_solution()

def test_1():
	assert get_checksum(get_lines('day2/input_test_2.txt')) == 9
