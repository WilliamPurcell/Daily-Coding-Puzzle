class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        '''
        ALGORITHM GrayCode(n)
        {
            if n == 1 return [0, 1]

            // generate Gray codes of order n-1 recursively 
            out  ← ... // add code here 

            for j ← len(out) - 1 downto 0  
                  // prepend 1 in front of out[j]   
                  // append the result to out   
            return out
        }
        '''
        if n == 1:
            return [0, 1]

        out= self.grayCode(n-1)
        for i in range(len(out)-1,-1,-1):
            out.append(out[i] | 1<<(n-1))
        return out



