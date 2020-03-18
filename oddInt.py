# Given an array, find the integer that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

def find_it(seq):
	for num in seq:
		count = 1
		index = seq.index(num) + 1
		while index < len(seq):
			if seq[index] == num:
				count += 1
			index += 1
		if count % 2 == 1:
			return num