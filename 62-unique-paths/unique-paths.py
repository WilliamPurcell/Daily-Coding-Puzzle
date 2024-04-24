class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        import numpy as np
        T = np.zeros((m, n))

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    T[i, j] = 1  # Base Case
                else:
                    T[i, j] = T[i-1, j] + T[i, j-1] 
        return int(T[m-1, n-1])
        
        