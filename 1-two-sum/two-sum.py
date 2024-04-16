class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_copy=nums[:]
        nums.sort()
        
        i=0
        j=len(nums)-1
        t=0
        v=len(nums)-1

        while (i<j) :
            sum = nums[i]+nums[j]
            if (sum == target):
                while (nums[i] != nums_copy[t]):
                    t+=1
                while (nums[j] != nums_copy[v]):
                    v-=1
                return t,v

            if (sum < target):
                i+=1
            else :
                j-=1
        
    