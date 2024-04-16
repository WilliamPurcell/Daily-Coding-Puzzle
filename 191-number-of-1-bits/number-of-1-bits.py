class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if (n==0):
            return 0
        if((n & 1) == 1):
            return 1 + self.hammingWeight(n>>1)
        return self.hammingWeight(n>>1)
        
        