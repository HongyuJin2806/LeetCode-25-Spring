class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == "":
            return 0

        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i = 1
        elif s[0] == '+':
            i = 1

        output = 0
        while i < len(s) and s[i].isdigit():
            output = output * 10 + int(s[i])
            i += 1

        output *= sign
        if output < -2 ** 31:
            return -2 ** 31
        elif output > 2 ** 31 - 1:
            return 2 ** 31 - 1

        return output