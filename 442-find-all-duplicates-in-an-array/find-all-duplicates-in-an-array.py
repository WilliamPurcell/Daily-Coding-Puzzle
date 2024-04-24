class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ht = [0] * (n + 1)
        duplicates = []

        for num in nums:
            ht[num] += 1

        for i in range(1, n + 1):
            if ht[i] > 1:
                duplicates.append(i)

        return duplicates
        