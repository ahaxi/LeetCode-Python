class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        n,loop=0,x
        while int(loop/10):
            n=n*10+loop%10
            loop/=10
        n=n*10+loop%10
        return n==x   
