#!/usr/bin/python

#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    for i in range(0,(len(s)-1)):
        s=s[:i] + s[i].swapcase() + s[i+1:]
    return s

if __name__ == '__main__':
  swap_case("Ashish")
