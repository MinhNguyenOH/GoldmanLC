class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        value = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000
                 }
        for i in range(len(s)):
            if i + 1 < len(s) and value[s[i]] < value[s[i+1]]:
                res -= value[s[i]]
            else:
                res += value[s[i]]

        return res
