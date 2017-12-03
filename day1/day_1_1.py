#!/usr/bin/python3

import fileinput

def get_lines(file_name):
	return fileinput.input(files=(file_name))

def get_sum(string):
	count = 0
	current_index = 0
	next_index = 0
	string_len = len(string)

	for i in range(0, string_len):
		current_index = i
		next_index = i + 1

		if next_index >= string_len:
			next_index = 0

		if string[next_index] == string[current_index]:
			count += int(string[current_index])

	return count

def print_solution():
	for line in get_lines('input.txt'):
		print(get_sum(line.strip()))

print_solution()

def test_1():
	for line in get_lines('day1/input_test_1.txt'):
		assert get_sum(line.strip()) == 3

def test_2():
	for line in get_lines('day1/input_test_2.txt'):
		assert get_sum(line.strip()) == 4

def test_3():
	for line in get_lines('day1/input_test_3.txt'):
		assert get_sum(line.strip()) == 0

def test_4():
	for line in get_lines('day1/input_test_4.txt'):
		assert get_sum(line.strip()) == 9
