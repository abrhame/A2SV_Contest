class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = n
        j = 0
        nums = sorted(set(nums))

        for i in range(len(nums)):
            while j < len(nums) and nums[j] < nums[i] + n:
                j += 1

            temp = j - i
            count = min(count, n - temp)

        return count