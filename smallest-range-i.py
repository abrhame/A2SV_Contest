class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_nums = max(nums)
        min_nums = min(nums)

        return max(0,(max_nums - k) - (min_nums + k))