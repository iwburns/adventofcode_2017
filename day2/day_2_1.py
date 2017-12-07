#!/usr/bin/python3

import fileinput
import re

def get_lines(file_name):
	return fileinput.input(files=(file_name))

def get_checksum(lines):
	total = 0

	for line in lines:
		line = re.split(r'\t+| +', line.rstrip('\n'))
		line = list(map(int, line))

		largest = int(max(line))
		smallest = int(min(line))

		total += (largest - smallest)

	return total

def print_solution():
	print(get_checksum(get_lines('day2/input.txt')))

print_solution()

def test_1():
	assert get_checksum(get_lines('day2/input_test_1.txt')) == 18
