def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 0
        found = -1
        for index in range(0,len(s)):
            new_sub_str = s[0:index] + s[index+1:]
            if str(s[index]) not in new_sub_str:
                found = index
                break
        return found
