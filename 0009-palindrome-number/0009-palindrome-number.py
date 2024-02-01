class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        if x_str[::-1]  == x_str:
            return True
        else:
            return False