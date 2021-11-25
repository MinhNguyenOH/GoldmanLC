class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        index = 0
        for i in s:

            if dict[i] == 1:
                return index
            index += 1
        return -1
