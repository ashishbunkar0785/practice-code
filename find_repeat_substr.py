/*
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
https://leetcode.com/problems/repeated-substring-pattern/
*/

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp_str=""
        return_flag=False
        for index in range(0,len(s)):
            char = s[index]
            #print char
            temp_str=temp_str + char
            print temp_str
            print(s[index+1:(index + 1 + len(temp_str))])
            if temp_str == s[index+1:(index + 1 + len(temp_str))]:
                return_flag=True
                for i in range(index+len(temp_str)+1,len(s),len(temp_str)):
                    print("in if:", i)
                    print(s[i:i+len(temp_str)])
                    if temp_str == s[i:i+len(temp_str)]:
                        return_flag=True
                        #print(s[i+len(temp_str)])
                        continue
                    else:
                        return_flag=False
                        #temp_str = ""
                        break
                #if len(s) > (index + len(temp_str)) and len
            if return_flag == True:
               return True
            print "------------------------------------------------------"
        return return_flag
