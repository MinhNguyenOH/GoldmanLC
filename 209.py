class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        res = 0
        length = len(nums) + 1
        for i in range(len(nums)):
            res += nums[i]
            while (res >= target and left <= i):
                length = min(length, i - left + 1)
                res -= nums[left]
                left += 1
        if length == len(nums) + 1:
            return 0
        return length
