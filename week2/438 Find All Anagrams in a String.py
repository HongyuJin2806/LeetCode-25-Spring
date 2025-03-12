class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []

        p_count = [0] * 26
        s_count = [0] * 26

        for char in p:
            p_count[ord(char) - ord('a')] += 1

        for i in range(len(p) - 1):
            s_count[ord(s[i]) - ord('a')] += 1

        result = []

        for i in range(len(p) - 1, len(s)):
            s_count[ord(s[i]) - ord('a')] += 1

            if p_count == s_count:
                result.append(i - len(p) + 1)

            s_count[ord(s[i - len(p) + 1]) - ord('a')] -= 1

        return result