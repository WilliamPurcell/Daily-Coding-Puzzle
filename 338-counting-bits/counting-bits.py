class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans =[0]*(n+1)
        for i in range(n+1):
            ans[i]= ans [(i/2)] + i % 2

        return ans
        