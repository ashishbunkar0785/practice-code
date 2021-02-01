"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        temp_str = s
        for char in t:
            if str(char) not in temp_str:
                return False
            else:
                i = 0
                str_len = len(temp_str)
                while(i < str_len):
                    if temp_str[i] == char:
                        temp_str = temp_str[0:i] + temp_str[i+1:str_len]
                        break
                    i = i + 1
        return True
