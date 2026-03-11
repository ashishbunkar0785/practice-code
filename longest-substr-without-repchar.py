#!/usr/bin/env python
import sys
'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

#input_str = "abcabcbb"
input_str = sys.argv[1]
longest_str = ""
longest_str_len = 0
temp_str = ""
start_index = 0

while(start_index < len(input_str)):
    char = input_str[start_index]
    if char not in longest_str:
        longest_str = longest_str + str(char)
        longest_str_len = longest_str_len + 1
        start_index = start_index + 1
    else:
        if temp_str == "" or len(temp_str) < longest_str_len:
            temp_str = longest_str
        longest_str = ""
        longest_str_len = 0
        index = input_str[0:start_index].rindex(char)
        start_index = index + 1

if len(temp_str) > len(longest_str):
    print "longest substr:" +temp_str
else:
    print "longest substr:" +longest_str
