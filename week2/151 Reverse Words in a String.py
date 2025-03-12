class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split()
        return " ".join(word_list[::-1])