class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum = 0
        self.x = x
        if x == 0:
            return 0
        elif x > 0:
            rev = 0
            while(x > 0):
                rem = x % 10
                rev = (rev * 10) + rem
                x = x /10
            return rev if rev < 2147483647 else 0
        else:
            x = 0-x
            rev = 0
            while(x > 0):
                rem = x % 10
                rev = (rev * 10) + rem
                x = x /10
            return (0-rev) if rev < 2147483647 else 0
            
        
            
