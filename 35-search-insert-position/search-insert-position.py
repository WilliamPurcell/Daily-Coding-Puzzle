class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right= len(nums)-1

        while left<= right:
            current = left + right

            if nums[current] == target:
                return current
            elif nums[current] < target:
                left = current + 1
            else:
                right = current -1
        return left

        