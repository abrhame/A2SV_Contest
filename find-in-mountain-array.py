class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        def findPeak():
            left, right = 0, mountain_arr.length() - 1
            while left < right:
                mid = (left + right) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left

        def binary_search(target, start, end):
            left, right = start, end

            while left <= right:  # Change from 'while left < right' to 'while left <= right'
                mid = (left + right) // 2
                if mountain_arr.get(right) == target:
                    return right
                m = mountain_arr.get(mid)
                if m == target:
                    return mid
                elif m < target:
                    left = mid + 1
                else:
                    right = mid - 1 # Fix the adjustment of 'right'
            return -1

        peak = findPeak()
        start, end = 0, peak
        search = binary_search(target, start, end)
        if search != -1:
            return search
        
        start, end = peak + 1, mountain_arr.length() - 1
        search = binary_search(target, start, end)
        return search