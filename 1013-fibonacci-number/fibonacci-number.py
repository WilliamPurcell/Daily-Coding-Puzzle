class Solution(object):
    def fib(self, n):
        #Recursize
        '''
        if (n==0 or n ==1):
            return n
        out1 = self.fib(n-1)
        out2 = self.fib(n-2)
        return out1+ out2
        '''
        
        #NonRecursive
        '''
        FA=[]
        FA.append(0)
        FA.append(1)

        for i in range(2,n+1):
            FA.append(FA[i-1]+FA[i-2])
        return FA[n]
        '''

        #O(1) Memory
        FA=[]
        FA.append(0)
        FA.append(1)
        if (n==0):
            return FA[0]

        for i in range(2,n+1):
            temp=FA[1]
            FA[1]= FA[1]+FA[0]
            FA[0]=temp
            del temp
        return FA[1]
