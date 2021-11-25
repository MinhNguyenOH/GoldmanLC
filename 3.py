class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = res = 0
        for r in range(len(s)):
            while s[r] in seen:
                del seen[s[l]]
                l += 1
            seen[s[r]] = 1
            res = max(res, r - l + 1)
        return res
