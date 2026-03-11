#!/usr/bin/python3

#Program to find if first string is an anagram of second
#

import sys

first_string = sys.argv[1]
second_string=sys.argv[2]

if len(first_string) != len(second_string):
	print "Not Anagram"
	sys.exit(0)

temp_str=second_string

for char in first_string:
	if (temp_str.find(str(char))) == -1:
		print "Not anagram"
		sys.exit(0)
	else:
		index=temp_str.find(str(char))
		temp_str = temp_str[0:index] + temp_str[(index + 1):]

print "Anagram"
