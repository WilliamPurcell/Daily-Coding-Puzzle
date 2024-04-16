class Solution(object):
    def climbStairs(self, n):
        
        #Recursize
        '''
        if (n==0 or n ==1 or n==2):
            return n
        out1 = self.climbStairs(n-1)
        out2 = self.climbStairs(n-2)
        return out1+ out2
        '''
    
        #NonRecursive
        '''
        FA=[]
        FA.append(0)
        FA.append(1)
        for i in range(2,n+2):
            FA.append(FA[i-1]+FA[i-2])
        return FA[n+1]
        '''
        
        #O(1) Memory
        if (n==0 or n ==1 or n==2):
            return n
        FA=[]
        FA.append(0)
        FA.append(1)
        for i in range(1,n+1):
            temp=FA[1]
            FA[1]= FA[1]+FA[0]
            FA[0]=temp
            del temp
        return FA[1]
        