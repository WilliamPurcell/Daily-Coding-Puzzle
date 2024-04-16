class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        #Brute Force
        '''
        value =1
        if n==0:
            return 1
        if n>0:
            for i in range (n):
                value= value*x
        if n<0:
            for i in range (abs(n)):
                value= value*x
            value=1/value 
        return value
        '''

        #recursive decrease-by-one 
        '''
        if n==0:
            return 1
        elif n < 0:
            value =x * self.myPow(x, abs(n) - 1)
            return 1/value
        return x* self.myPow(x,n-1)
        ''' 
        #recursive decrease-by-half solution
        
        if n==0:
            return 1
        elif n<0:
            n=-n
            x=1/x
        if n%2==0:
            return self.myPow(x*x,n/2)
        else :
            return x*self.myPow(x,n-1)
         
        